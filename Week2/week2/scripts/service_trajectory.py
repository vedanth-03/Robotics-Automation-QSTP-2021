#!/usr/bin/env python

import rospy
import numpy as np
from week2.srv import Trajectory, TrajectoryResponse
from std_msgs.msg import Float32, Float32MultiArray

class TrajectoryObj:
    def __init__(self, request):
        self.x = request.x
        self.y = request.y
        self.theta = request.theta
        self.v = request.v
        self.w = request.w

        # Store the points of the trajectory to plot
        self.x_points = [self.x]
        self.y_points = [self.y]

    def step(self):
        dt = 0.05
        n = 50
        x = self.x
        y = self.y
        theta = self.theta
        for i in range(n):
            x_t = self.v*(np.cos(theta))
            y_t = self.v*(np.sin(theta))
            theta_t = self.w

            x += x_t*dt
            y += y_t*dt
            theta += theta_t*dt

            self.x_points.append(x)
            self.y_points.append(y)


def calc_trajectory(request):
    obj = TrajectoryObj(request)
    obj.step()
    return {'x_points': obj.x_points, 'y_points': obj.y_points}

def server():
    service = rospy.Service('calc_trajectory', Trajectory, calc_trajectory)
    rospy.spin()      

if __name__ == "__main__":
    rospy.init_node('server_trajectory')
    try:
        server()
    except:
        pass