#!/usr/bin/env python

import sys
input= sys.stdin.readline

N,K = map(int,input().split())
li = [list(map(int,input().split())) for _ in range(N)]
visit = [0 for _ in range(N)]
visit[K] = 1
ans=10*9
for k in range(N):
    for i in range(N):
        for j in range(N):
            li[i][j] = min(li[i][j], li[i][k] + li[k][j])

def fmin(cur, cost, cnt):
    global ans
    if N == cnt:
        ans = min(ans, cost)
        return
    for i in range(N):
        if visit[i] == 0:
            visit[i] = 1
            fmin(i, cost + li[cur][i], cnt+1)
            visit[i] = 0
fmin(K, 0, 1)
print(ans)
