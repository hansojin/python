#!/usr/bin/env python

n=int(input())

dp=[0,2,4]
x=3
for i in range(3,n+1):
    dp.append(dp[i-1]+x)
    if i%3!=0:
        x+=1
print(dp[n])
