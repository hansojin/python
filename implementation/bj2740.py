#!/usr/bin/env python

import sys
input = sys.stdin.readline

n, m = map(int,input().split())
A = [list(map(int,input().split())) for i in range(n)]
m, k = map(int,input().split())
B = [list(map(int,input().split())) for i in range(m)]

for i in range(n):
    res = []
    for l in range(k):
        a = 0
        for j in range(m):
            a += A[i][j] * B[j][l]
        res.append(a)
    print(*res)
