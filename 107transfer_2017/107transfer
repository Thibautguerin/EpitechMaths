#!/usr/bin/python3

#
# EPITECH PROJECT, 2018
# 107transfer.py
# File description:
# main for 107transfer
#

from math import *
import re
import sys

if (len(sys.argv) % 2 == 0 and sys.argv[1] != "-h"):
    exit(84)

string = (" ".join(sys.argv))
regexp = r"^(./107transfer((( ([+-]?[0-9]*[*]?)+)+)|( -h)))$"

if re.match(regexp, string) is None:
    exit(84)

if sys.argv[1] == "-h":
    print("USAGE")
    print("             ./107transfer [num den]*")
    print("")
    print("DESCRIPTION")
    print("             num  polynominal numerator defined by its coeficients")
    print("             den  polynominal denominator defined by its coeficients")
else:
    i = int(1)
    j = float(0.000)
    res = float(0.00000)
    res2 = float(0.00000)
    resf = float(1.00000)
    
    while (round(j, 3) <= float(1.000)):
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
        if (j == 0):
            print(0,"->",'{:.5f}'.format(resf))
        elif (j >= 1):
            print(1,"->",'{:.5f}'.format(resf))
        else:
            print(round(j, 3),"->",'{:.5f}'.format(resf))
        resf = 1
        j = j + 0.001
        i = 1
exit(0)
