#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def publisher_w():
    rospy.init_node("publisher_world")
    pub = rospy.Publisher('world', String, queue_size=1)
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        pub.publish("World!")
        rate.sleep()

if __name__ == "__main__":
    try:
        publisher_w()
    except  rospy.ROSInterruptException:
        pass
