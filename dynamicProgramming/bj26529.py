#!/usr/bin/env python

dp=[0 for _ in range(47)]
dp[0]=1
dp[1]=1

for i in range(2,46):
    dp[i]=dp[i-1]+dp[i-2]

for i in range(int(input())):
    n=int(input())
    print(dp[n])
