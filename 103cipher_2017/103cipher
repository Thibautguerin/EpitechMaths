#!/usr/bin/python2

#
# EPITECH PROJECT, 2017
# 103cipher.py
# File description:
# main for 103cipher
#

from __future__ import print_function
from math import *
import re
import sys

string = (" ".join(sys.argv))

regexp = r"^(./103cipher [0-9 ]+ (.)+ 1)|(./103cipher (.+){2} 0)$"
    
if re.match(regexp, string) is None:
    exit(84)

print("Key matrix :")
    
n = int(0)
    
while len(sys.argv[2]) > pow(n, 2):
    n = n + 1

i = int(0)
j = int(0)
nbc = n
if sys.argv[3] == "0":
    while len(sys.argv[2]) != pow(n, 2):
        sys.argv[2] = sys.argv[2] + chr(0)

    while len(sys.argv[1])%n != 0:
        sys.argv[1] = sys.argv[1] + chr(0)

if sys.argv[3] == "0":
    while n != 0 :
        while i <= (j+nbc-1):
            if i == (j+nbc-1):
                print('{:<0}'.format(ord(sys.argv[2][i])),end="")
            else:
                print('{:<10}'.format(ord(sys.argv[2][i])),end=" ")
            i = i + 1
        print("\n",end="")
        j = j + nbc
        n = n - 1
        
print("\n",end="")

if sys.argv[3] == "0":
    print("Encrypted message :")
elif sys.argv[3] == "1":
    print("Decrypted message :")


n = int(0)

while len(sys.argv[2]) > pow(n, 2):
    n = n + 1
    
nbl = int(ceil(len(sys.argv[1])/n))
nbc = n
i = int(0)
j = int(0)
res = int(0)
nbc1 = n

if sys.argv[3] == "0":
    while nbl != 0:
        while nbc1 != 0:
            while nbc != 0:
                res = res + ord(sys.argv[1][i]) * ord(sys.argv[2][j])
                i = i + 1
                j = j + n
                nbc = nbc - 1
            if nbl == 1 and nbc == 0 and nbc1 == 1:
                print(res)
            else:
                print(res,end=" ")
            res = 0
            i = i - n
            j = j - n * n + 1
            nbc = n
            nbc1 = nbc1 - 1
        nbc1 = n
        j = 0
        i = i + n
        nbl = nbl - 1
exit(0)
