#!/usr/bin/env python

import sys
input= sys.stdin.readline

li = [0,0] + [1] * 1000001

for i in range(2, 1001):
    j = 2
    if li[i] == 1:
        while i * j <= 1000000:
            li[i * j] = 0
            j += 1

arr = [i for i in range(1000001) if li[i] == 1]

while True:
    n = int(input())
    if n == 0:
        break
    for i in arr:
        if li[n - i] == 1:
            print(f"{n} = {i} + {n - i}")
            break
