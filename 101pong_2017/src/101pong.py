#!/usr/bin/python2.7

#
# EPITECH PROJECT, 2017
# 101pong.py
# File description:
# main for 101pong
#

from __future__ import print_function
from math import *
import sys
import os

x0 = float(sys.argv[1])
y0 = float(sys.argv[2])
z0 = float(sys.argv[3])
x1 = float(sys.argv[4])
y1 = float(sys.argv[5])
z1 = float(sys.argv[6])
n = int(sys.argv[7])

def error_msg():
    print("/!\Error, make sure you put your arguments as follows :")
    print("./101pong x0 y0 z0 x1 y1 z1 n\n")
    print("x0 -> ball abscissa at time t - 1")
    print("y0 -> ball ordinate at time t - 1")
    print("z0 -> ball altitude at time t - 1")
    print("x1 -> ball abscissa at time t")
    print("y1 -> ball ordinate at time t")
    print("z1 -> ball altitude at time t")
    print("n -> time shift (greater than or equal to zero, integer)")
    sys.exit(84)

if len(sys.argv) == 8 and n > 0:
    vectorX = '{:.2f}'.format(x1 - x0)
    vectorY = '{:.2f}'.format(y1 - y0)
    vectorZ = '{:.2f}'.format(z1 - z0)

    vectorX1 = '{:.2f}'.format(float(vectorX) * (n + 1) + x0)
    vectorY1 = '{:.2f}'.format(float(vectorY) * (n + 1) + y0)
    vectorZ1 = '{:.2f}'.format(float(vectorZ) * (n + 1) + z0)

    angle = '{:.2f}'.format(90 - (acos(fabs(float(vectorZ)) / sqrt(pow(float(vectorX), 2) + pow(float(vectorY), 2) + pow(float(vectorZ), 2))) * 180 / pi))

    print("The speed vector coordinates are :")
    print('(',vectorX,';',vectorY,';',vectorZ,')',sep='')
    print("At time t+",n,", ball coordinates will be :",sep='')
    print('(',vectorX1,';',vectorY1,';',vectorZ1,')',sep='')

    if (y0 < 0 or y1 < 0 or z0 < 0 or z1 < 0 or angle == "0.00" or angle == "90.00"):
        print("The ball won't reach the bat.")
    else:
        print("The incidence angle is :")
        print(angle,"degrees")
    sys.exit(0)

else:
    error_msg()
