#!/usr/bin/env python

import sys
input = sys.stdin.readline

n=int(input())
li=[]
for _ in range(n):
    x,y=map(int,input().split())
    li.append([x,y])

li.sort(key=lambda x: x[0])

dp=[1]*n

for i in range(n):
    for j in range(i):
        if li[i][1]>li[j][1]:
            dp[i]=max(dp[i],dp[j]+1)

print(n-max(dp))
