#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32

rospy.init_node('publisher_radius')
pub = rospy.Publisher('radius', Float32, queue_size=1)

rate = rospy.Rate(1)
radius = 1.0

while not rospy.is_shutdown():
    try:
        pub.publish(radius)
        rate.sleep()
    except:
        pass