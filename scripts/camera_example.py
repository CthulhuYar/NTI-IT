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
    dir = [0, 0, 0]
    dir[0] = (laser[570]+laser[580]+laser[560])/3
    dir[1] = (laser[300]+laser[290]+laser[310])/3
    dir[2] = (laser[30]+laser[40]+laser[20])/3
    return dir

def check():
    robot = Robot()
    laser = robot.getLaser()



def distance_read():
    direct = laser_read()
    sect = [round(direct[0] / 0.6, 3), round(direct[1] / 0.6, 3), round(direct[2] / 0.6, 3)]
    return(sect)


def move(dist, angle):
    WHEEL_RADIUS = 0.09
    dist_left = (dist / WHEEL_RADIUS)
    init_enc = robot.getEncoders().get('left')

    while abs(dist_left) > 0.005:
        enc = robot.getEncoders().get("left")
        dist_left = init_enc + (dist * 1.0 / WHEEL_RADIUS) - enc
        up = 0.1 * dist_left
        up = (up if up > -0.3 else -0.3) if up < 0.3 else 0.3

        # trave to the angle
        current_dir = robot.getDirection()
        e = (target_dir - current_dir + 9.42) % 6.28 - 3.14
        up_ang = e * 0.5
        up_ang = (up_ang if up_ang > -0.3 else -0.3) if up_ang < 0.3 else 0.3

        robot.setVelosities(up, up_ang)

        # some delay for don't overload computation
        robot.sleep(0.001)

    robot.setVelosities(0, 0)


if __name__ == "__main__":
    robot = Robot()
    robot.setVelosities(0, 0)
    robot.sleep(1)

    # print(object_color)
    speed = 0.5
    angular_speed = 0.5

    min_d = distance_read()[0] + distance_read()[2]
    while True:

        while distance_read()[1] > 1:
            robot.setVelosities(speed, 0)
            print(distance_read())

            if min_d > distance_read()[0] + distance_read()[2]:
                min_d = distance_read()[0] + distance_read()[2]
                print(min_d)
        robot.setVelosities(0, 0)
        obj = camera_analyzing()
        if obj == "RED":
            print(obj)
            robot.setVelosities(0, 0)
            robot.sleep(1)
            exit(1)
        robot.setVelosities(0, angular_speed)
        print(distance_read())
        robot.sleep(1)

    robot.setVelosities(0, 0)
    robot.sleep(0.1)
    exit(1)
