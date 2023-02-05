#!/usr/bin/env python

import sys
input = sys.stdin.readline

a,b=map(int,input().split())

arr = []
for i in range(a):
    arr.append(list(str(input())))

if arr[0][0]=='W':
    for i in range(a):
        for j in range(b):
            

