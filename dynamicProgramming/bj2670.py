#!/usr/bin/env python

import sys
input = sys.stdin.readline

li=[]
n=int(input())
for _ in range(n):
    li.append(float(input()))

for i in range(1,n):
    li[i]=max(li[i],li[i]*li[i-1])
print('%0.3f'%max(li))

