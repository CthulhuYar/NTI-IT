#!/usr/bin/env python3

import math
import sys
from robot_library.robot import *
import rospy
import cv2
import numpy as np
from time import time
from copy import deepcopy

'''
Green - 8 0 0 107 255 255
Blue - 88 68 0 255 255 255
Red - 0 239 185 17 255 255
Yellow - 15 203 93 58 255 255
'''


def camera_analyzing():
    global image
    robot = Robot()
    img = robot.getImage()
    image = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    def input_color(color):
        global image
        img = deepcopy(image)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        # переносим значения из массива в переменные
        h1 = color[0]
        s1 = color[1]
        v1 = color[2]
        h2 = color[3]
        s2 = color[4]
        v2 = color[5]
        h_min = np.array((h1, s1, v1), np.uint8)
        h_max = np.array((h2, s2, v2), np.uint8)
        thresh = cv2.inRange(hsv, h_min, h_max)
        moments = cv2.moments(thresh, 1)
        dM01 = moments['m01']
        dM10 = moments['m10']
        dArea = moments['m00']
        return int(dArea)

    Green = [50, 20, 20, 107, 255, 255]
    Blue = [88, 68, 0, 255, 255, 255]
    Red = [0, 239, 115, 17, 255, 255]
    Yellow = [15, 203, 93, 58, 255, 255]

    array = ["GREEN", "BLUE", "RED", "YELLOW"]
    mas = [input_color(Green), input_color(Blue), input_color(Red), input_color(Yellow)]
    # print(mas)
    return array[mas.index(max(mas))]


def laser_read():
    robot = Robot()
    laser = robot.getLaser()
    laser = laser.get('values')[40:len(laser.get('values')) - 40]
    dir = [0, 0, 0, 0, 0]
    dir[0] = (laser[600]+laser[595]+laser[602])/3  # Left 90
    dir[1] = ((laser[470] + laser[465] + laser[475]) / 3)  # Left 45
    dir[2] = (laser[340] + laser[345] + laser[335]) / 3  # Center
    dir[3] = ((laser[210] + laser[215] + laser[205]) / 3)  # Right 45
    dir[4] = (laser[0]+laser[5]+laser[10])/3  # Right 90
    for i in range(len(dir)):
        dir[i]/=0.6

    return dir


if __name__ == "__main__":
    robot = Robot()
    robot.setVelosities(0, 0)
    angular_speed = 0.2
    speed = 0.5
    robot.sleep(1)
    k = 0
    while True:
        while camera_analyzing() != "YELLOW":
            robot.setVelosities(0, angular_speed)
            # print(camera_analyzing())
        robot.setVelosities(0, 0)
        print("found")
        if 0:  # Condition of fonding the marker
            robot.setVelosities(0, 0)
            print("found marker")

        while laser_read()[4] < 0.4 or laser_read()[3] < 0.6:
             robot.setVelosities(0, -angular_speed)

        if laser_read()[2] > 1:
            robot.setVelosities(speed, 0)
            robot.sleep(3)
        else:
            robot.setVelosities(-speed, 0)
            robot.sleep(1.5)
        k+=1
        if k==4:
            break


    robot.setVelosities(0, 0)

    exit(1)
