#!/usr/bin/env python

import sys
input = sys.stdin.readline

a,b=map(int,input().split())
li=list(map(int,input().split()))

prefix_sum=[0]
tmp=0

for i in li:
    tmp+=i
    prefix_sum.append(tmp)


lis=[]
for i in range(a-b):
    lis.append(prefix_sum[i+b]-prefix_sum[i])

print(max(lis))

