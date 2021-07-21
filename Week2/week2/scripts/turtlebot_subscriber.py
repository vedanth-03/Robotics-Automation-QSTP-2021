#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32
from week2.srv import AngularVelocity
from geometry_msgs.msg import Twist

def callback(msg):
    r = msg.data
    rospy.wait_for_service('compute_ang_vel')
    try:
        vel_calc = rospy.ServiceProxy('compute_ang_vel', AngularVelocity)
        service_res = vel_calc(r)
        ang_vel = service_res.AngVel
        rate = rospy.Rate(10)
        while not rospy.is_shutdown():
            t = Twist()
            t.linear.x = 0.1
            t.angular.z = ang_vel
            pub.publish(t)
            rate.sleep()

    except rospy.ServiceException:
        pass


def sub_setup():
    sub = rospy.Subscriber('radius', Float32, callback)
    rospy.spin()

if __name__ == "__main__":
    rospy.init_node("Subscriber")
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
    try:
        sub_setup()
    except:
        pass