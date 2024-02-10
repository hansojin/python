#!/usr/bin/env python

import sys
input= sys.stdin.readline

a = list(map(int, input().split()))
answer = [1, 2, 3, 4, 5]

while True:
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
            print(*a)

    if a == answer:
        break
