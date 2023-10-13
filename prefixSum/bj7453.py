#!/usr/bin/env python

import sys
input= sys.stdin.readline
def find():
    AB = dict()
    for a in A:
        for b in B:
            AB[a+b] = AB.get(a+b, 0)+1
    res = 0
    for c in C:
        for d in D:
            res += AB.get(-(c + d), 0)
    return res

N = int(input())
A, B, C, D = [], [], [], []
for _ in range(N):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)
print(find())
