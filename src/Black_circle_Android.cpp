// Detects a Red circle and plots its center and circumference
//Live feed is from the android phone
//getting erratic values for circle area

#include <ros/ros.h>
#include <image_transport/image_transport.h>
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
 //String face_cascade_name = "/home/aj/catkin_ws/src/beginner_tutorials/src/haarcascade_frontalface_alt.xml";
 /*CascadeClassifier face_cascade;
 string window_name = "Capture - Face detection";
 string window_name2 = "Mask Result";
 
 RNG rng(12345);*/

/*int count = 0;
double area_old=0, area_new;
double center_x_old=0, center_x_new;
double diff_area, diff_centroid;
*/
string window_name = "Circle Detection";
string window_name2 = "Canny";
static const std::string OPENCV_WINDOW = "Image window";
float area;
class ImageConverter
{
  ros::NodeHandle nh_;
  image_transport::ImageTransport it_;
  image_transport::Subscriber image_sub_; // subscriber object
  image_transport::Publisher image_pub_;  // Publisher object
   
public:
  ImageConverter()
    : it_(nh_)
  {
    // Subscribe to input video feed and publish output video feed
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
     
     Mat src,src_gray,detected_edges;
     src = cv_ptr->image;   // GETTING IMAGE HERE 
     medianBlur(src,src, 3);
     Mat hsv_image;
   cvtColor(src, hsv_image, cv::COLOR_BGR2HSV);
   Mat lower_red_hue_range;
   Mat upper_red_hue_range; 
   inRange(hsv_image, cv::Scalar(0, 100, 100), cv::Scalar(10, 255, 255), lower_red_hue_range);
   inRange(hsv_image, cv::Scalar(160, 100, 100), cv::Scalar(180, 255, 255), upper_red_hue_range);

  Mat red_hue_image;
  addWeighted(lower_red_hue_range, 1.0, upper_red_hue_range, 1.0, 0.0, red_hue_image);
  GaussianBlur(red_hue_image, red_hue_image, cv::Size(9, 9), 2, 2);
 // Canny( detected_edges, detected_edges,120,250,3 );
  //imshow( window_name2,detected_edges);

  vector<cv::Vec3f> circles;
  HoughCircles(red_hue_image, circles, CV_HOUGH_GRADIENT, 1,red_hue_image.rows/8, 100, 20, 10, 0);

  for(size_t current_circle = 0; current_circle < circles.size(); ++current_circle) 
  {
   Point center(round(circles[current_circle][0]),round(circles[current_circle][1]));
   int radius = round(circles[current_circle][2]);
   circle(src, center, radius, cv::Scalar(0, 255, 0), 3);
   circle( src, center, radius, Scalar(0,0,255), 3, 8, 0 );
   area = 3.14*radius*radius;
   cout<<"Area=  "<<area<<"\n";   
 }

  imshow( window_name,src);
  waitKey(3);
   
   }
   };
 
 /** @function main */
 int main( int argc, char** argv )
 {
  //if( !face_cascade.load( face_cascade_name ) ){ printf("--(!)Error loading\n"); return -1;};
  ros::init(argc, argv, "image_converter");
  ImageConverter ic;
  ros::spin();
  return 0;
 }


