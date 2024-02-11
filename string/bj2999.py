#!/usr/bin/env python

import sys
input= sys.stdin.readline

str = input().rstrip()
len = len(str)

x, y = 0, 0

for i in range(1, int(len / 2) + 1):
    for j in range(i, len + 1):
        if i * j == len:
            x, y = i, j

for i in range(x):
    for j in range(y):
        print(str[i + j * x], end='')
