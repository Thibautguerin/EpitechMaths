#!/usr/bin/python3

#
# EPITECH PROJECT, 2018
# 108trigo.py
# File description:
# main for 108trigo
#

from math import *
import re
import sys

if (len(sys.argv) == 1):
    exit(84)

if ((sqrt(len(sys.argv) - 2)) != int(sqrt(len(sys.argv) - 2)) or ((len(sys.argv) - 2) == 1)):
    exit(84)

string = (" ".join(sys.argv))
regexp = r"^(./108trigo (((EXP|COS|SIN|COSH|SINH)( [+-]?[0-9]+)+)|(-h)))$"

if re.match(regexp, string) is None:
    exit(84)

if sys.argv[1] == "-h":
    print("USAGE")
    print("             ./107trigo fun a0 a1 a2....")
    print("")
    print("DESCRIPTION")
    print("             fun  function to be applied, among at least EXP, COS, SIN, COSH and SINH")
    print("             ai   coeficients of the matrix")
else:
    n = int(0)
    temp = int(0)

    k = int(0)

    while len(sys.argv) - 2 > pow(k, 2):
        k = k + 1

    savek = k
    nbl = k
    nbc = k
    i = int(2)
    j = int(2)
    nbc1 = k
    matrix = []
    var = int(0)
    x = int(0)
    parse = int(1)

    while (len(sys.argv) - 2 > var):
        var = var + 1
        matrix.append(float(0))
    
    while (n != 50):
        temp = n
        while (temp != -1):
            while nbl != 0:
                while nbc1 != 0:
                    while nbc != 0:
                        if parse == 1:
                            matrix[i - 2] = float(float(matrix[i - 2]) + float(sys.argv[i]) * float(sys.argv[j]))
                        else:
                            matrix[i - 2] = float(float(matrix[i - 2]) * float(sys.argv[j]))
                        i = i + 1
                        j = j + k
                        nbc = nbc - 1
                    i = i - k
                    j = j - k * k + 1
                    nbc = k
                    nbc1 = nbc1 - 1
                nbc1 = k
                j = 2
                i = i + k
                nbl = nbl - 1
            temp = temp - 1
            k = savek
            nbl = k
            nbc = k
            i = 2
            j = 2
            nbc1 = k
            parse = 0
        while (x != pow(k, 2)):
            matrix[x] = float(float(matrix[x]) * (1/factorial(n)))
            x = x + 1
        x = 0
        n = n + 1
print(matrix)
exit(0)
