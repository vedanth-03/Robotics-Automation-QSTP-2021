#!/usr/bin/env python

import rospy
from std_msgs.msg import String

class Hello:
    def __init__(self):
        self.pub = rospy.Publisher('helloworld', String, queue_size=1)
        self.sub1 = rospy.Subscriber('hello', String, self.callback1)
        self.sub2 = rospy.Subscriber('world', String, self.callback2)
        self.str = String()
        self.str1 = None
        self.str2 = None
    
    def callback1(self,msg):
        self.str1 = msg.data
        self.str = f"{str(self.str1)} {str(self.str2)}"
        self.pub.publish(self.str)

    def callback2(self,msg):
        self.str2 = msg.data
        self.str = f"{str(self.str1)} {str(self.str2)}"
        self.pub.publish(self.str)
        

if __name__ == "__main__":
    rospy.init_node('fullname')
    hello = Hello()
    rospy.spin()

