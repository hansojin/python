#!/usr/bin/env python

import sys
input= sys.stdin.readline

N = int(input())
li = [0] * N
j = 0

for i in range(N):
    D, C = input().split()
    f = int(C)

    if D == 'jinju':
        j = f
    li[i] = f

cnt = 0
for f in li:
    if j < f:
        cnt += 1

print(j)
print(cnt)
