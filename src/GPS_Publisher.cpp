#include <ros/ros.h>
#include <string>
#include <geometry_msgs/PoseArray.h>
#include <sensor_msgs/JointState.h>
#include <tf/transform_broadcaster.h>
#include <geometry_msgs/Vector3.h>
#include <stdlib.h>
#include <math.h>
#include <nav_msgs/Odometry.h>

double vl = 10.0; // velocity of the wheels
double vr = 78.0;
class GPS
{
public:
	GPS(); 
        void GPS_pub_function();  
private:
	ros::NodeHandle n; 
	ros::Publisher GPS_pub; 
					
};

void GPS::GPS_pub_function()
{
geometry_msgs::Vector3 GPS;
GPS.x = vl;
GPS.y = vr;
GPS_pub.publish(GPS);
}

GPS::GPS() //constructor
{

	GPS_pub = n.advertise<geometry_msgs::Vector3>("GPS",100); 
        
}

int main(int argc, char** argv)
{
ros::init(argc, argv, "GPS");
GPS k;
while(ros::ok())
{
k.GPS_pub_function();
}
ros::spin();
}

