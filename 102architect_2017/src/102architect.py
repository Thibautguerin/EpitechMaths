#!/usr/bin/python2

#
# EPITECH PROJECT, 2017
# 102architect.py
# File description:
# main for 102architect
#

from __future__ import print_function
from math import *
import re
import sys

string = (" ".join(sys.argv))

regexp = r"^./102architect [+-]?[0-9]*[\.]?[0-9]+ [+-]?[0-9]*[\.]?[0-9]+(( -[th]( [+-]?[0-9]*[\.]?[0-9]+){2})|( -[rs]( [+-]?[0-9]*[\.]?[0-9]+)))+$"

if re.match(regexp, string) is None:
    exit(84)
    
i = int(0)

while i != len(sys.argv):
    if sys.argv[i] == "-t":
        print("Translation by the vector (",sys.argv[i+1],", ",sys.argv[i+2],")",sep="")
    if sys.argv[i] == "-h":
        print("Homothety by the ratios ",sys.argv[i+1]," and ",sys.argv[i+2],sep="")
    if sys.argv[i] == "-r":
        print("Rotation at a ",sys.argv[i+1]," degree angle",sep="")
    if sys.argv[i] == "-s":
        print("Symmetry about an axis inclined with an angle of ",sys.argv[i+1]," degrees",sep="")
    i = i + 1

x = float(sys.argv[1])
y = float(sys.argv[2])
x1 = '{:.2f}'.format(float(sys.argv[1]))
y1 = '{:.2f}'.format(float(sys.argv[2]))

l3c1 = '{:.2f}'.format(float(0))
l3c2 = '{:.2f}'.format(float(0))
l3c3 = '{:.2f}'.format(float(1))
    
if sys.argv[3] == "-t":
    l1c1 = '{:.2f}'.format(float(1))
    l1c2 = '{:.2f}'.format(float(0))
    l1c3 = '{:.2f}'.format(float(sys.argv[4]))
    l2c1 = '{:.2f}'.format(float(0))
    l2c2 = '{:.2f}'.format(float(1))
    l2c3 = '{:.2f}'.format(float(sys.argv[5]))    
elif sys.argv[3] == "-h":
    l1c1 = '{:.2f}'.format(float(sys.argv[4]))
    l1c2 = '{:.2f}'.format(float(0))
    l1c3 = '{:.2f}'.format(float(0))
    l2c1 = '{:.2f}'.format(float(0))
    l2c2 = '{:.2f}'.format(float(sys.argv[5]))
    l2c3 = '{:.2f}'.format(float(0))
elif sys.argv[3] == "-r":
    l1c1 = '{:.2f}'.format(float(cos(float(sys.argv[4])/180*pi)))
    l1c2 = '{:.2f}'.format(float(-sin(float(sys.argv[4])/180*pi)))
    l1c3 = '{:.2f}'.format(float(0))
    l2c1 = '{:.2f}'.format(float(sin(float(sys.argv[4])/180*pi)))
    l2c2 = '{:.2f}'.format(float(cos(float(sys.argv[4])/180*pi)))
    l2c3 = '{:.2f}'.format(float(0))
elif sys.argv[3] == "-s":
    l1c1 = '{:.2f}'.format(float(cos(float(sys.argv[4])/180*pi*2)))
    l1c2 = '{:.2f}'.format(float(sin(float(sys.argv[4])/180*pi*2)))
    l1c3 = '{:.2f}'.format(float(0))
    l2c1 = '{:.2f}'.format(float(sin(float(sys.argv[4])/180*pi*2)))
    l2c2 = '{:.2f}'.format(float(-cos(float(sys.argv[4])/180*pi*2)))
    l2c3 = '{:.2f}'.format(float(0))

x1, y1 = '{:.2f}'.format(float(float(l1c1) * float(x1) + float(l1c2) * float(y1) + float(l1c3))), '{:.2f}'.format(float(float(l2c1) * float(x1) + float(l2c2) * float(y1) + float(l2c3))) 
    
i = int(4)
    
while i != len(sys.argv):
    if sys.argv[i] == "-t":
        l1c1 = '{:.2f}'.format(float(l1c1))
        l1c2 = '{:.2f}'.format(float(l1c2))
        l1c3 = '{:.2f}'.format(float(float(l1c1) * float(sys.argv[i+1]) + float(l1c2) * float(sys.argv[i+2]) + float(l1c3))) 
        l2c1 = '{:.2f}'.format(float(l2c1))
        l2c2 = '{:.2f}'.format(float(l2c2))
        l2c3 = '{:.2f}'.format(float(float(l2c1) * float(sys.argv[i+1]) + float(l2c2) * float(sys.argv[i+2]) + float(l2c3)))
        x1, y1 = '{:.2f}'.format(float(float(l1c1) * float(x1) + float(l1c2) * float(y1) + float(l1c3))), '{:.2f}'.format(float(float(l2c1) * float(x1) + float(l2c2) * float(y1) + float(l2c3)))
    elif sys.argv[i] == "-h":
        l1c1 = '{:.2f}'.format(float(float(l1c1) * float(sys.argv[i+1]))) 
        l1c2 = '{:.2f}'.format(float(float(l1c2) * float(sys.argv[i+2])))
        l1c3 = '{:.2f}'.format(float(l1c3))
        l2c1 = '{:.2f}'.format(float(float(l2c1) * float(sys.argv[i+1])))
        l2c2 = '{:.2f}'.format(float(float(l2c2) * float(sys.argv[i+2])))
        l2c3 = '{:.2f}'.format(float(l2c3))
        x1, y1 = '{:.2f}'.format(float(float(l1c1) * float(x1) + float(l1c2) * float(y1))), '{:.2f}'.format(float(float(l2c1) * float(x1) + float(l2c2) * float(y1)))
    elif sys.argv[i] == "-r":
        l1c1 = '{:.2f}'.format(float(float(l1c1) * float(cos(float(sys.argv[i+1])/180*pi)) + float(l1c2) * float(sin(float(sys.argv[i+1])/180*pi))))
        l1c2 = '{:.2f}'.format(float(float(l1c1) * float(-sin(float(sys.argv[i+1])/180*pi)) + float(l1c2) * float(cos(float(sys.argv[i+1])/180*pi))))
        l1c3 = '{:.2f}'.format(float(l1c3))
        l2c1 = '{:.2f}'.format(float(float(l2c1) * float(cos(float(sys.argv[i+1])/180*pi)) + float(l2c2) * float(sin(float(sys.argv[i+1])/180*pi))))
        l2c2 = '{:.2f}'.format(float(float(l2c1) * float(-sin(float(sys.argv[i+1])/180*pi)) + float(l2c2) * float(cos(float(sys.argv[i+1])/180*pi))))
        l2c3 = '{:.2f}'.format(float(l2c3))
        x1, y1 = '{:.2f}'.format(float(float(l1c1) * float(x1) + float(l1c2) * float(l1c3) + float(l1c3))), '{:.2f}'.format(float(float(l2c1) * float(x1) + float(l2c2) * float(l2c3) + float(l2c3)))
    elif sys.argv[i] == "-s":
        l1c1 = '{:.2f}'.format(float(float(l1c1) * float(cos(float(sys.argv[i+1])/180*pi*2)) + float(l1c2) * float(sin(float(sys.argv[i+1])/180*pi*2))))
        l1c2 = '{:.2f}'.format(float(float(l1c1) * float(sin(float(sys.argv[i+1])/180*pi*2)) + float(l1c2) * float(-cos(float(sys.argv[i+1])/180*pi*2))))
        l1c3 = '{:.2f}'.format(float(l1c3))
        l2c1 = '{:.2f}'.format(float(float(l2c1) * float(cos(float(sys.argv[i+1])/180*pi*2)) + float(l2c2) * float(sin(float(sys.argv[i+1])/180*pi*2))))
        l2c2 = '{:.2f}'.format(float(float(l2c1) * float(sin(float(sys.argv[i+1])/180*pi*2)) + float(l2c2) * float(-cos(float(sys.argv[i+1])/180*pi*2))))
        l2c3 = '{:.2f}'.format(float(l2c3))
        x1, y1 = '{:.2f}'.format(float(float(l1c1) * float(x1) + float(l1c2) * float(l1c3) + float(l1c3))), '{:.2f}'.format(float(float(l2c1) * float(x1) + float(l2c2) * float(l2c3) + float(l2c3)))
    i = i + 1
    
line1 = '{:<10} {:<10} {:<0}'.format(l1c1, l1c2, l1c3)
line2 = '{:<10} {:<10} {:<0}'.format(l2c1, l2c2, l2c3)
line3 = '{:<10} {:<10} {:<0}'.format(l3c1, l3c2, l3c3)

print(line1)
print(line2)
print(line3)

print("(",sys.argv[1],",",sys.argv[2],") => (",x1,",",y1,")",sep="")

exit(0)
