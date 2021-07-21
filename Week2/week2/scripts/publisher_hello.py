#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def publisher_h():
    rospy.init_node("publisher_hello")
    pub = rospy.Publisher('hello', String, queue_size=1)
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        pub.publish("Hello,")
        rate.sleep()

if __name__ == "__main__":
    try:
        publisher_h()
    except  rospy.ROSInterruptException:
        pass
