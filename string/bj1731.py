#!/usr/bin/env python

import sys
input= sys.stdin.readline

li=[]
n=int(input())
for _ in range(n):
    li.append(int(input()))


if li[1]*li[1]==li[0]*li[2]:
    print(li[-1]*(li[-1]//li[-2]))
else:
    print(li[-1]+(li[1]-li[0]))
