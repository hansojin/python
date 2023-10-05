#!/usr/bin/env python

import math

def squares(n):
   # if sqrt(n) is integer
    if int(math.sqrt(n))==math.sqrt(n):
           return 1
    # if sqrt(n-i^2) is integer
    for i in range(1,int(math.sqrt(n))+1):
        if int(math.sqrt(n-i**2))==math.sqrt(n-i**2):
            return 2
    # if sqrt(n-i^2-j^2) is integer
    for i in range(1,int(math.sqrt(n))+1):
        for j in range(1,int(math.sqrt(n-i**2))+1):
            if int(math.sqrt(n-i**2-j**2))==math.sqrt(n-i**2-j**2):
                return 3
    # else, 4
    return 4
  
n=int(input())
print(squares(n))
