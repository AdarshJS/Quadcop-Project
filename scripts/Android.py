#!/usr/bin/env python

# Python libs
import sys, time
# numpy and scipy
import numpy as np
#from scipy.ndimage import filters
# OpenCV
import cv2
# Ros libraries
import roslib
import rospy
from sensor_msgs.msg import CompressedImage

VERBOSE=False

#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#fourcc = cv2.cv.CV_FOURCC(*'XVID')
#out = cv2.VideoWriter('output.avi',fourcc, 20.0,(640,480))

class image_feature:

    def __init__(self):
        self.subscriber = rospy.Subscriber("/camera/image/compressed",CompressedImage, self.callback,  queue_size = 1)
       
    def callback(self, ros_data):
        
        np_arr = np.fromstring(ros_data.data, np.uint8) #fromstring converts string to image
        image_np = cv2.imdecode(np_arr, cv2.CV_LOAD_IMAGE_COLOR)
        #out.write(image_np)
        cv2.imshow('cv_img', image_np)
        cv2.waitKey(2)

        
def main(args):
    '''Initializes and cleanup ros node'''
    ic = image_feature()
    rospy.init_node('image_feature', anonymous=True)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print "Shutting down ROS Image feature detector module"
    #out.release()
    cv2.destroyAllWindows()
    

if __name__ == '__main__':
    main(sys.argv)
