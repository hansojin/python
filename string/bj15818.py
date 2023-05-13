#!/usr/bin/env python

import sys
input =sys.stdin.readline
from functools import reduce

n,r=map(int,input().split())
li=list(map(int,input().split()))

def multiply(arr):
    return reduce(lambda x, y:x*y,arr)

print(multiply(li)%r)
