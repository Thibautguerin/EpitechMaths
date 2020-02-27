#!/usr/bin/python3

#
# EPITECH PROJECT, 2017
# 103cipher.py
# File description:
# main for 104intersection
#

from __future__ import print_function
from math import *
import re
import sys

string = (" ".join(sys.argv))

regexp = r"^(./104intersection (1|2|3)( [+-]?[0-9]*){7})|(./104intersection -h)$"
    
if re.match(regexp, string) is None:
    exit(84)

if float(sys.argv[8]) <= 0:
    exit(84)
    
if float(sys.argv[1]) == 3 and float(sys.argv[8]) >= 90:
    exit(84)

if sys.argv[1] == "-h":
    print("\nUSAGE:\n\n./104intersection opt xp yp zp xv yv zv p\n")
    print("opt          number of the option : 1 for a sphere, 2 for a cylinder, 3 for a cone")
    print("xp, yp, zp   coordinates of the point by which the light ray goes through")
    print("xv, yv, zv   coordinates of the direction vector of the light ray")
    print("p            parameter : radius of the sphere, radius of the cylinder\n                      or angle formed by the cone and the Z-axis.")
    exit(0)
    
xp = float(sys.argv[2])
yp = float(sys.argv[3])
zp = float(sys.argv[4])
xv = float(sys.argv[5])
yv = float(sys.argv[6])
zv = float(sys.argv[7])
p = float(sys.argv[8])
    
if sys.argv[1] == "1":
    print("sphere of radius",sys.argv[8])
elif sys.argv[1] == "2":
    print("cylinder of radius",sys.argv[8])
else:
    print("cone of",sys.argv[8],"degree angle")
    
print("straight line going through the (",sys.argv[2],',',sys.argv[3],',',sys.argv[4],") point and of direction vector (",sys.argv[5],',',sys.argv[6],',',sys.argv[7],')',sep="")

if ((xp == p and yp == 0 and xv == 0 and yv == 0) or (yp == p and xp == 0 and xv == 0 and yv == 0)) and sys.argv[1] == "2":
    print("There is an infinite number of intersection points.")
else:
    if sys.argv[1] == "1":
        a = float(pow(xv, 2) + pow(yv, 2) + pow(zv, 2))
        b = float(2*xv*xp + 2*yv*yp + 2*zv*zp)
        c = float(pow(xp, 2) + pow(yp, 2) + pow(zp, 2) - pow(p, 2))
    elif sys.argv[1] == "2":
        a = float(pow(xv, 2) + pow(yv, 2))
        b = float(2*xv*xp + 2*yv*yp)
        c = float(pow(xp, 2) + pow(yp, 2) - pow(p, 2))
    else:
        a = float(pow(1/tan(radians(p)), 2) * (pow(xv, 2) + pow(yv, 2)) - pow(zv, 2))
        b = float(pow(1/tan(radians(p)), 2) * (2*xv*xp + 2*yv*yp) - 2*zv*zp)
        c = float(pow(1/tan(radians(p)), 2) * (pow(xp, 2) + pow(yp, 2)) - pow(zp, 2))
    
    delta = int(pow(b, 2) - 4*a*c)

    if delta > 0:
        print("2 intersection points :")
        k1 = float((-b+sqrt(delta))/(2*a))
        k2 = float((-b-sqrt(delta))/(2*a))
        x1 = '{:.3f}'.format(float(k1*xv+xp))
        y1 = '{:.3f}'.format(float(k1*yv+yp))
        z1 = '{:.3f}'.format(float(k1*zv+zp))
        print('(',x1,", ",y1,", ",z1,')',sep="")
        x2 = '{:.3f}'.format(float(k2*xv+xp))
        y2 = '{:.3f}'.format(float(k2*yv+yp))
        z2 = '{:.3f}'.format(float(k2*zv+zp))
        print('(',x2,", ",y2,", ",z2,')',sep="")
    elif delta == 0:
        print("1 intersection point :")
        k = float(-b/(2*a))
        x = '{:.3f}'.format(float(k*xv+xp))
        y = '{:.3f}'.format(float(k*yv+yp))
        z = '{:.3f}'.format(float(k*zv+zp))
        print('(',x,", ",y,", ",z,')',sep="")
    else:
        print("No intersection point.")
        
exit(0)
