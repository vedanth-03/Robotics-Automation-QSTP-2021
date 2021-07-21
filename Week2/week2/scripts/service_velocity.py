#!/usr/bin/env python

import rospy
from week2.srv import AngularVelocity, AngularVelocityResponse

def ang_vel(request):
    r = request.radius
    AngVel = 0.1/r
    try:
        return AngularVelocityResponse(AngVel)
    except:
        pass

def server():
    service = rospy.Service('compute_ang_vel', AngularVelocity, ang_vel)
    rospy.spin()

if __name__ == "__main__":
    rospy.init_node("server_velocity")
    try:
        server()
    except:
        pass
