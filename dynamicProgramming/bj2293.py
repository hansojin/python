#!/usr/bin/env python

n,k=map(int,input().split())
c=[int(input()) for i in range(n)]
dp=[0]*(k+1)
dp[0]=1

for coin in c:
    for i in range(coin,k+1):
        if i-coin>=0:
            dp[i]+=dp[i-coin]
            '''
            coin들로 i 원 만들기 = i-coin 후 coin 추가
            '''
print(dp[k])
