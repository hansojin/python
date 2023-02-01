#!/usr/bin/env python

import sys
input= sys.stdin.readline

n=int(input())
nums=[]

for i in range(n):
    nums.append(list(map(int,input().rstrip().split())))
nums.sort()

for a,b in nums:
    print(a,b)
