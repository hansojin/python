#!/usr/bin/env python

import sys
input = sys.stdin.readline

n=int(input())
num=list(map(int,input().split()))
li=[0]*n
cnt=0
for i in range(n):
    if num[i]>0:
        li[cnt]+=num[i]
    else:
        cnt+=1
        li[cnt]=num[i]
        cnt+=1
del li[cnt:]

print(max(li))
