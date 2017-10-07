/* This code gets video feed from Android phone 
   Performs face detection and publishes the velocity commands to the BBB 
   to give to the KK2 board. 
   Values 6.0, 7.5 and 9.0 are taken to limit the value given to the KK2 board  
*/

#include <ros/ros.h>
#include <image_transport/image_transport.h>
#include <geometry_msgs/Vector3.h>
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
 String face_cascade_name = "/home/aj/catkin_ws/src/beginner_tutorials/src/haarcascade_frontalface_alt.xml";
 CascadeClassifier face_cascade;
 string window_name = "Capture - Face detection";
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
    quad_vel_pub = nh_.advertise<geometry_msgs::Vector3>("Quad_vel",100);
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

   geometry_msgs::Vector3 quad_vel;

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
     //pyrDown( frame,frame, Size( frame.cols/2, frame.rows/2 ) );
     std::vector<Rect> faces;
     Mat frame_gray;
     cvtColor( frame, frame_gray, CV_BGR2GRAY );
     equalizeHist( frame_gray, frame_gray );

     //-- Detect faces
     face_cascade.detectMultiScale(frame_gray, faces, 1.1, 2, 0|CV_HAAR_SCALE_IMAGE, Size(30, 30));
     Mat mask = Mat::zeros(Size(frame.cols, frame.rows), CV_8UC3);
    if(faces.size() > 0)
    {
     for( size_t i = 0; i < faces.size(); i++ )
     {
       Point center( faces[i].x + faces[i].width*0.5, faces[i].y + faces[i].height*0.5 );
       rectangle( frame,Point(faces[i].x,faces[i].y),Point(faces[i].x + faces[i].width, faces[i].y + faces[i].height),Scalar(255, 255, 255),1,8);
       rectangle( mask,Point(faces[i].x,faces[i].y),Point(faces[i].x + faces[i].width, faces[i].y + faces[i].height),Scalar(255, 255, 255),-1,8);
      area = faces[i].width*faces[i].height;
      centroid = center.x;
      //for pitch
      if(area>0 && area<2800)
           quad_vel.x = 9.0;  //forward
     
      else if(area>4500)
           quad_vel.x = 6.0;  //backward
      
      else
           quad_vel.x = 7.5;  //stay
      
      if(centroid>0 && centroid<270)
         quad_vel.y = 6.0;   //move left
      
      else if(centroid>370)
         quad_vel.y = 9.0;   //move right
      
      else
         quad_vel.y = 7.5;   //stay     
      
      cout<<"Area=  "<<area<<"\t Cent=  "<<centroid<<"\n"; 
      quad_vel_pub.publish(quad_vel);
      }}
    else 
    {
     quad_vel.x = 7.5;
     quad_vel.y = 7.5;
     quad_vel_pub.publish(quad_vel);
    }
   Mat res;
   bitwise_and(frame,mask,res);
   imshow( window_name, frame );
   imshow( window_name2, res );
   waitKey(3);
   }
   }
   };
 
 /** @function main */
 int main( int argc, char** argv )
 {
  if( !face_cascade.load( face_cascade_name ) ){ printf("--(!)Error loading\n"); return -1;};
  ros::init(argc, argv, "image_converter");
  ImageConverter ic;
  ros::spin();
  return 0;
 }


