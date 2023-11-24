#!/usr/bin/env python

import sys
input= sys.stdin.readline

s=set()
for _ in range(int(input())):
    a,b=map(int,input().split())
    for i in range(a,b):
        s.add(i)
print(len(s))
