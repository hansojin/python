#!/usr/bin/env python

n=int(input())
dp=[0]*10000
li=[0]*10000
for i in range(n):
    li[i]=int(input())

dp[0]=li[0]
dp[1]=li[0]+li[1]
dp[2]=max(li[2]+li[0],li[2]+li[1],dp[1])

for i in range(3,n):
    dp[i]=max(li[i]+li[i-1]+dp[i-3],li[i]+dp[i-2],dp[i-1])
print(max(dp))
