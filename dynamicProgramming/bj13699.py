#!/usr/bin/env python

dp=[1,1,2]
n=int(input())
for i in range(3,n+1):
    tmp=0
    for j in range(0,i):
        tmp+=dp[j]*dp[i-j-1]
    dp.append(tmp)
print(dp[n])
