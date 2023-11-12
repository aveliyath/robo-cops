#! /usr/bin/env python3

import socket
import time

HOST = "192.168.1.10"
PORT_UR = 30002
PORT_GRIPPER = 63352

# Create socket connection to robot arm and gripper
s_ur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_ur.connect((HOST, PORT_UR))

s_gripper = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_gripper.connect((HOST, PORT_GRIPPER))

# send move joint command  to robot arm
command_ur = "movej([0,0,0,0,0,0])"
# movej([baseJointValue, shoulderJointValue, ...], acceleration, velocity, time, blend_radius)
#   with JointValues in rad
#        accelartion in rad/s^2 (otpional)
#        velocity of leading axis in rad/s (otpional)
#        time in s to make the move, 0 means not specified (optional)
#        blend_radius in m (optional)
# 
#  movej([0, -1.57, 0, 0, 0, 0]): go to upright position
 
s_ur.send (str.encode((command_ur + "\n")))

# send activate gripper command
s_gripper.sendall(b'SET ACT 1\n')
time.sleep(1)
# set requested postion to 255 (value between 0-255)
s_gripper.send(b'SET POS 255\n')
# make the gripper move 
s_gripper.send(b'SET GTO 1\n')
time.sleep(2)

# close the connections
s_ur.close()
s_gripper.close()