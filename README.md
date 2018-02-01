# Quadcop-Project
Quadcopter with an android phone that recognizes criminals and gives GPS coordinates while in hot pursuit.

The Quadcop can be controlled by an on-board Raspberry PI 3 or BeagelBone Black/Green that give PWM signals to the flight controller board. The user communicates with the quadcopter using a gaming joystick connected to a laptop. The on-board computer receives the control signals through Wifi and passes it to the Flight controller board (KK2, CC3D, PIxhawk etc.)  

There are multiple C++ and Python programs in this repo that accomplish this task. The codes are relatively simple to understand, but requires prerequisites in ROS and OpenCV. I used ROS Indigo for this implementation. OpenCV codes should work for the latest version.

Just add the src and scripts folder to your ROS package. Compare your Cmakelists and package.xml to make the appropriate dependencies. 

7_Display.py initiates the GUI that was developed for the view the Quadcopter's attitude, and the video feed from the Android phone. Connect a gaming joystick before running this program. 
