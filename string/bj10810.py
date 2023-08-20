#!/usr/bin/env python

import sys
input = sys.stdin.readline

n,m=map(int,input().split())
li=[0 for _ in range(n)]

for _ in range(m):
    s,e,b=map(int,input().split())
    for i in range(s,e+1):
        li[i-1]=b
print(*li)
