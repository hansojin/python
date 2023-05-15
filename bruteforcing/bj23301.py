#!/usr/bin/env python

import sys

input = sys.stdin.readline

time = [0 for _ in range(1001)]
n, m = map(int, input().split())
for _ in range(n):
    for _ in range(int(input())):
        start, end = map(int, input().split())
        for i in range(start, end):
            time[i] += 1

maxx = -1
x, y = 0, 0
for i in range(0, 1001-m):
    tmp = sum(time[i:i+m])
    if tmp > maxx:
        maxx = tmp
        x, y = i, i+m
    elif tmp == maxx and i < x:
        x, y = i, i+m
print(x, y)
