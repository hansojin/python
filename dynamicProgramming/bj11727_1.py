#!/usr/bin/env python

dp=[0,1,3]
n=int(input())
for i in range(3,n+1):
    dp.append(dp[i-1]+2*dp[i-2])
print(dp[n]%10007)