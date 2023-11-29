#!/usr/bin/env python

import sys
input= sys.stdin.readline

n=int(input())
s=set()
for _ in range(2*n-1):
    m=input()
    if m in s:
        s.remove(m)
    else:
        s.add(m)

for i in s:
    print(i)

