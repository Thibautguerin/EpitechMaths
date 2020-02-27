#!/usr/bin/python3

#
# EPITECH PROJECT, 2018
# 105torus.py
# File description:
# main for 105torus
#

from __future__ import print_function
from math import *
import re
import sys

string = (" ".join(sys.argv))

regexp = r"^(./105torus [1-3]( [+-]?[0-9]+){5} [0-9]+)$"
    
if re.match(regexp, string) is None:
    exit(84)

a1 = float(sys.argv[6])
a2 = float(sys.argv[5])
a3 = float(sys.argv[4])
a4 = float(sys.argv[3])
a5 = float(sys.argv[2])
pre = int(sys.argv[7])
x = float(1);
debut = float(0)
end = float(1)
yd = float(a1*pow(debut,4) + a2*pow(debut,3) + a3*pow(debut,2) + a4*debut + a5)
ye = float(a1*pow(end,4) + a2*pow(end,3) + a3*pow(end,2) + a4*end + a5)
y = float(a1*pow(x,4) + a2*pow(x,3) + a3*pow(x,2) + a4*x + a5)
v1 = float(yd)
v2 = float(ye)
i = int(0)

if sys.argv[1] == "1":
    while (round(y, pre) != round(0, pre)):
        x = debut + (end - debut) / 2
        y = float(a1*pow(x,4) + a2*pow(x,3) + a3*pow(x,2) + a4*x + a5)
        if (round(y, pre) == round(0, pre)):
            exit(0)
        else:
            if (round(x, pre) != x):
                print("x =",'{0:.{1}f}'.format(x, pre))
            else :
                print("x =",round(x, pre))
        yd = float(a1*pow(debut,4) + a2*pow(debut,3) + a3*pow(debut,2) + a4*debut + a5)
        ye = float(a1*pow(end,4) + a2*pow(end,3) + a3*pow(end,2) + a4*end + a5)
        if (y > 0 and yd < 0):
            end = x
        elif (y < 0 and ye > 0):
            debut = x
        elif (y > 0 and ye < 0):
            debut = x
        elif (y < 0 and yd > 0):
            end = x
        y = float(a1*pow(x,4) + a2*pow(x,3) + a3*pow(x,2) + a4*x + a5)
        i = i + 1
        if (i == 59):
            exit(84)
        
elif sys.argv[1] == "2":

    exit(0)

else:

    exit(0)
    
exit(0)
