#!/usr/bin/env python

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = []

for i in range(n):
    a = list(map(int, input().split()))
    arr.append(a)
   
dp=[[0]*(n+1) for i in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        dp[i][j]=dp[i][j-1]+dp[i-1][j]-dp[i-1][j-1]+arr[i-1][j-1]
        # dp는 표 0행0열에 0을 추가로 넣어줬으니까 1부터 시작이 맞는데
        # arr는 0부터 값이 들어가 있으니까 -1해주는게 맞음

for _ in range(m):
    x1,y1,x2,y2=map(int,input().split())

    ans=dp[x2][y2]-dp[x2][y1-1]-dp[x1-1][y2]+dp[x1-1][y1-1]

    print(ans)
