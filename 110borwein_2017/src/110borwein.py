#!/usr/bin/python3
#
# EPITECH PROJECT, 2018
# 110borwein.py
# File description:
# main for 110borwein
#

from decimal import Decimal
from math import *
import sys
import re

def print_usage():
    print("USAGE")
    print("           ./110borwein n\n")
    print("DESCRIPTION")
    print("           n    constant defining the integral to be computed")

def error_management():
    string = (" ".join(sys.argv))
    regexp = r"^(./110borwein [0-9]+)$"

    if (len(sys.argv) != 2):
        exit(84)
    if sys.argv[1] == "-h":
        print_usage()
        exit(0)
    if re.match(regexp, string) is None:
        exit(84)

def rectangles(start, end, subdiv):
    h = float((end - start) / subdiv)
    res = float(0)
    x = float(start)
    
    while(x < end):
        res += borwein(x, int(sys.argv[1]))
        x += h
    res = res * h
    print("I",sys.argv[1]," = ",'{:.10f}'.format(res),sep='')
    diff = Decimal(res - (pi / 2))
    if (str('{:.10f}'.format(diff)) == "-0.0000000000"):
        diff = diff * (-1)
    print("diff = ",'{:.10f}'.format(diff),sep='')

def trapezoids(start, end, subdiv):
    h = float((end - start) / subdiv)
    res = float(0)
    x = float(start)
    
    while(x < end):
        res += (borwein(x, int(sys.argv[1])) + borwein(x+h, int(sys.argv[1])))/2
        x += h
    res = res * h
    print("I",sys.argv[1]," = ",'{:.10f}'.format(res),sep='')
    diff = float(res - (pi / 2))
    if (str('{:.10f}'.format(diff)) == "-0.0000000000"):
        diff = diff * (-1)
    print("diff = ",'{:.10f}'.format(diff),sep='')

def borwein(x, n):
    res = float(0)
    n = n - 1

    if (x == 0):
        res = float(1)
    else:
        res = (sin((x)/(2*n+1)))/((x)/(2*n+1))
        while (n >= 0):
            res = (res) * (sin((x)/(2*n+1))/((x)/(2*n+1)))
            n = n - 1
    return (res)

def main():
    error_management()
    print("Rectangles:")
    rectangles(0, 5000, 10000)
    print("\nTrapezoids:")
    trapezoids(0, 5000, 10000)
    print("\nSimpson:")
    trapezoids(0, 5000, 10000)
    exit(0)

main()
