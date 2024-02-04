#!/usr/bin/env python

import sys
input = sys.stdin.readline

dp = [1,2,4,7]
li=[]
for i in range(int(input())):
    n = int(input())
    li.append(n)

for i in range(4, max(li)):
    dp.append((dp[-3]+dp[-2]+dp[-1])%1000000009)

for i in li:
    print(dp[i-1])
