#!/usr/bin/env python

import sys
input= sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))
a = 0
res = []
for i in range(n-1):
    if li[i] < li[i+1]:
        a += li[i+1] - li[i]
    else:
        res.append(a)
        a = 0
res.append(a)
print(max(res))
