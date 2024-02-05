#!/usr/bin/env python

import sys
input= sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    li = list(map(int, input().split()))
    li.reverse()
    max = li[0]
    sum = 0

    for i in range(1, n):
        if max < li[i]:
            max = li[i]
            continue
        sum += max - li[i]

    print(sum)  
