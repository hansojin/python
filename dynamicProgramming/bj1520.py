#!/usr/bin/env python

import sys
input= sys.stdin.readline

n, m = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1]*m for _ in range(n)]

pos = ((-1, 0), (1, 0), (0, -1), (0, 1))

def dfs(x, y):
    if x == n-1 and y == m-1: return 1
    if dp[x][y] != -1: return dp[x][y]

    dp[x][y] = 0
    for dx, dy in pos:
        nx, ny = x + dx, y + dy
        if not (0 <= nx < n and 0 <= ny < m) or li[x][y] <= li[nx][ny]:
            continue
        dp[x][y] += dfs(nx, ny)

    return dp[x][y]

print(dfs(0, 0))

