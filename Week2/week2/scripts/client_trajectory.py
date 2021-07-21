#!/usr/bin/env python

import rospy
import sys
import numpy as np
import matplotlib.pyplot as plt
from week2.srv import Trajectory, TrajectoryRequest
from std_msgs.msg import Float32, Float32MultiArray

def plot(x,y):
    plt.title("Trajectory")
    plt.xlabel("X-Coordinates")
    plt.ylabel("Y-Coordinates")
    plt.plot(x, y, color="red", alpha=0.75)
    plt.grid()
    plt.show() 

if __name__ == "__main__":
    rospy.init_node('client')
    rospy.wait_for_service('calc_trajectory')
    calc_proxy = rospy.ServiceProxy('calc_trajectory', Trajectory)
    arg = sys.argv[1:6]
    arg1 = [float(i) for i in arg]
    req = TrajectoryRequest(arg1[0], arg1[1], arg1[2], arg1[3], arg1[4])
    calc_res = calc_proxy(req)
    x_points = calc_res.x_points
    y_points = calc_res.y_points

    plot(x_points,y_points)