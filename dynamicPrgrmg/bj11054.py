#!/usr/bin/env python

import sys
input=sys.stdin.readline

n=int(input())
li=list((map(int,input().split())))
rvrse=li[::-1]

dp=[1]*n
dr=[1]*n

for i in range(1,n):
    for j in range(i):
        if li[i]>li[j]:
            dp[i]=max(dp[i],dp[j]+1)
        if rvrse[i]>rvrse[j]:
            dr[i]=max(dr[i],dr[j]+1)
ans=[0]*n
for i in range(n):
    ans[i]=dp[i]+dr[n-i-1]-1

print(max(ans))
