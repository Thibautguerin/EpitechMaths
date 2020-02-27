#!/usr/bin/python3

#
# EPITECH PROJECT, 2018
# 107transfer.py
# File description:
# main for 107transfer
#

from math import *
from pylab import *
import re
import sys
import time

if (len(sys.argv) % 2 == 0 and sys.argv[1] != "-h"):
    exit(84)

string = (" ".join(sys.argv))
regexp = r"^(./107transfer((( [+-]?[0-9]+){2}( ([+-]?[0-9]*[*]?)+)+)|( -h)))$"

if re.match(regexp, string) is None:
    exit(84)

if sys.argv[1] == "-h":
    print("USAGE")
    print("             ./107transfer [lim1] [lim2] [num den]*")
    print("")
    print("DESCRIPTION")
    print("             num  polynominal numerator defined by its coeficients")
    print("             den  polynominal denominator defined by its coeficients")
    print("             lim  limitation of the calculation")
else:
    i = int(3)
    j = float(sys.argv[1])
    res = float(0.00000)
    res2 = float(0.00000)
    resf = float(1.00000)
    x = []
    y = []

    while (round(j, 3) <= float(sys.argv[2])):
        x.append(j)
        lenn = len(sys.argv)
        while (i != lenn):
            exp = sys.argv[i].split("*")
            k = 0
            len1 = len(exp)
            while (k != len1):
                if (k == 0):
                    res = res + int(exp[k])
                else:
                    res = res + int(exp[k]) * pow(j, k)
                k = k + 1
            i = i + 1
            exp1 = sys.argv[i].split("*")
            k = 0
            len2 = len(exp1)
            while (k != len2):
                if (k == 0):
                    res2 = res2 + int(exp1[k])
                else:
                    res2 = res2 + int(exp1[k]) * pow(j, k)
                k = k + 1
            i = i + 1
            if (res2 == 0):
                exit(0)
            resf = resf * (res / res2)
            res = 0
            res2 = 0
        y.append(resf)
        resf = 1
        j = j + 0.001
        i = 3
    plot(x, y, '-b')
    xlabel('x')
    ylabel('y')
    title('bonus for 107transfer')
    show()
exit(0)
