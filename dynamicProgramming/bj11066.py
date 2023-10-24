#!/usr/bin/env python

import sys
input= sys.stdin.readline

for _ in range(int(input())):
    n=int(input())
    li=[0]+list(map(int,input().split()))

    sli=[0 for _ in range(n+1)]

    for i in range(1,n+1):
        sli[i]=sli[i-1]+li[i]

    dp=[[0 for i in range(n+1)] for j in range(n+1)]
    for i in range(2,n+1):
        for j in range(1,n+2-i):
            dp[j][j+i-1] = min([dp[j][j+q] + dp[j+q+1][j+i-1] for q in range(i-1)]) +(sli[j+i-1] - sli[j-1])

    print(dp[1][n])


