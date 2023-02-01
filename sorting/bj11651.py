#!/usr/bin/env python

import sys
input= sys.stdin.readline

n=int(input())
nums=[]

for i in range(n):
    nums.append(list(map(int,input().rstrip().split())))
nums.sort(key=lambda x : x[1])

for a,b in nums:
    print(a,b)

