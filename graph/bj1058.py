#!/usr/bin/env python

import sys
input= sys.stdin.readline

n = int(input())
li = [list(input()) for _ in range(n)]

conn = [[0] * n for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if li[i][j] == "Y" or (li[i][k] == "Y" and li[k][j] == "Y"):
                conn[i][j] = 1

answer = 0
for row in conn:
    answer = max(answer, sum(row))
print(answer)
