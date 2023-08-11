#!/usr/bin/env python

N, A = int(input()), []
dp = [[0 for j in range (N)] for i in range(N)]
def f(x):
    if (x[0] == 'A'): return 1
    if (x[0] == 'T'): return 10
    if (x[0] == 'J'): return 11
    if (x[0] == 'Q'): return 12
    if (x[0] == 'K'): return 13
    return int(x[0])
for i in range(N): A.append(list(map(f, input().split())))
for i in range(N-1, -1, -1):
    for j in range(N):
        if (j-1 >= 0): dp[i][j] = max(dp[i][j], dp[i][j-1])
        if (i+1 < N): dp[i][j] = max(dp[i][j], dp[i+1][j])
        dp[i][j] += A[i][j]
print (dp[0][N-1])
