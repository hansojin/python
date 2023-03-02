#!/usr/bin/env python

n=int(input())
dp=[]*n
li=[]*n
for _ in range(n):
    li.append(int(input()))

dp[0]=li[0]
dp[1]=li[0]+li[1]
dp[2]=li[0]+li[2]

if n==0:
    print(dp[0])
    exit()
elif n==1:
    print(dp[1])
    exit()
elif n==2:
    print(dp[2])
    exit()

for i in range(3,n-1):
    dp[i]=max(dp[i-3]+li[i-1]+li[i],dp[i-2]+li[i])
print(dp[-1])
