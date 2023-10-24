#!/usr/bin/env python

import sys
input =sys.stdin.readline

n=int(input())
sch=[]
for i in range(n):
    sch.append(list(map(int,input().split())))

dp=[0 for i in range(n+1)]

for i in range(n):
    for j in range(i+sch[i][0],n+1):
        if dp[j]<dp[i]+sch[i][1]:
            dp[j]=dp[i]+sch[i][1]
print(dp[-1])
