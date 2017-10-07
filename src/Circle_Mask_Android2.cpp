/* This code gets video feed from Android phone 
   Performs circle detection and publishes the velocity commands to the BBB 
   to give to the KK2 board. 
   Values 6.0, 7.5 and 9.0 are taken to limit the value given to the KK2 board  
*/

//Change the area and centroid ranges

#include <ros/ros.h>
#include <image_transport/image_transport.h>
#include <geometry_msgs/Vector3.h>
#include <geometry_msgs/Twist.h>
#include <cv_bridge/cv_bridge.h>
#include <sensor_msgs/image_encodings.h>
#include "opencv2/objdetect/objdetect.hpp"
#include "opencv2/highgui/highgui.hpp"
#include "opencv2/imgproc/imgproc.hpp"
#include <iostream>
#include <stdio.h>

using namespace std;
using namespace cv;
 
 /** Global variables */
 String circle_cascade_name = "/home/aj/catkin_ws/src/beginner_tutorials/src/Circle_Cascade.xml";
 CascadeClassifier circle_cascade;
 string window_name = "Capture - Circle detection";
 string window_name2 = "Mask Result";
 static const std::string OPENCV_WINDOW = "Image window";
 RNG rng(12345);

int count = 0;
double area=0;
double centroid = 0;


class ImageConverter
{ 
  ros::Publisher quad_vel_pub; 
  ros::NodeHandle nh_;
  image_transport::ImageTransport it_;
  image_transport::Subscriber image_sub_; // subscriber object
  image_transport::Publisher image_pub_;  // Publisher object
   
public:
  ImageConverter()
    : it_(nh_)
  {
    quad_vel_pub = nh_.advertise<geometry_msgs::Twist>("Quad_vel_auto",100);
    image_sub_ = it_.subscribe("/camera/image", 0, &ImageConverter::imageCb, this); 
    namedWindow(OPENCV_WINDOW);
  }

  ~ImageConverter()
  {
    destroyWindow(OPENCV_WINDOW);
  }

  // CALLBACK FUNCTION 
  void imageCb(const sensor_msgs::ImageConstPtr& msg) 
  { 

   geometry_msgs::Twist quad_vel;

    cv_bridge::CvImagePtr cv_ptr;
    try
    {
      cv_ptr = cv_bridge::toCvCopy(msg, sensor_msgs::image_encodings::BGR8);
    }
    catch (cv_bridge::Exception& e)
    {
      ROS_ERROR("cv_bridge exception: %s", e.what());
      return;
    }
     
     Mat frame;
     frame = cv_ptr->image;
     ::count++;
     if(::count!=5)
     {}
     else
     {
     ::count=0;
     pyrDown( frame,frame, Size( frame.cols/2, frame.rows/2 ) );
     //pyrDown( frame,frame, Size( frame.cols/2, frame.rows/2 ) );
     std::vector<Rect> circles;
     Mat frame_gray;
     cvtColor( frame, frame_gray, CV_BGR2GRAY );
     equalizeHist( frame_gray, frame_gray );

     //-- Detect circles
     circle_cascade.detectMultiScale(frame_gray, circles, 1.1, 1, 0|CV_HAAR_SCALE_IMAGE, Size(30, 30));
     Mat mask = Mat::zeros(Size(frame.cols, frame.rows), CV_8UC3);
    if(circles.size()==1)
    {
       Point center( circles[0].x + circles[0].width*0.5, circles[0].y + circles[0].height*0.5 );
       rectangle( frame,Point(circles[0].x,circles[0].y),Point(circles[0].x + circles[0].width, circles[0].y + circles[0].height),Scalar(0,0, 255),3,8);
       rectangle( mask,Point(circles[0].x,circles[0].y),Point(circles[0].x + circles[0].width, circles[0].y + circles[0].height),Scalar(255, 255, 255),-1,8);
      area = circles[0].width*circles[0].height;
      centroid = center.x;
      

      //for pitch
      if(area>0 && area<3000)
           quad_vel.linear.x = -0.5;  //forward
     
      else if(area>13000)
           quad_vel.linear.x = 0.5;  //backward was 6.0
      
      else
           quad_vel.linear.x = 0;  //stay
      
      if(centroid>0 && centroid<100)
         quad_vel.linear.y = -1.0;   //move left
      
      else if(centroid>190)
         quad_vel.linear.y = 1.0;   //move right
      
      else
         quad_vel.linear.y = 0;   //stay     
      
      cout<<"Area=  "<<area<<"\t Cent=  "<<centroid<<"\n"; 
      quad_vel_pub.publish(quad_vel);
      }
    else 
    {
     quad_vel.linear.x = 0.0;
     quad_vel.linear.y = 0.0;
     quad_vel_pub.publish(quad_vel);
    }
   Mat res;
   bitwise_and(frame,mask,res);
   imshow(window_name, frame );
   imshow(window_name2, res );
   waitKey(3);
   }
   }
   };
 
 /** @function main */
 int main( int argc, char** argv )
 {
  if( !circle_cascade.load( circle_cascade_name ) ){ printf("--(!)Error loading\n"); return -1;};
  ros::init(argc, argv, "image_converter");
  ImageConverter ic;
  ros::spin();
  return 0;
 }


