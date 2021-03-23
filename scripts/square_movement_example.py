#!/usr/bin/env python3

import sys
from robot_library.robot import *
import cv2
import rospy
import numpy as np
import math

# initialize robot
robot = Robot()
# defining constant from simulator
def laser_read():
    laser = robot.getLaser()
    laser = laser.get('values')[40:len(laser.get('values')) - 40]
    dir = [0,0,0]
    dir[0] = round(laser[600], 3)
    dir[1] = round(laser[342], 3)
    dir[2] = round(laser[150], 3)
    return dir

if __name__ == "__main__":
    for iiii in range(999999):
        direct = laser_read()
        sect = [round(direct[0]/0.6, 3), round(direct[1]/0.6, 3), round(direct[2]/0.6, 3)]
        print(direct, sect)
    exit(1)