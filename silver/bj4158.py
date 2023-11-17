#!/usr/bin/env python

import sys
input= sys.stdin.readline

while True:
    n,m=map(int,input().split())
    if n==m==0:
        break
    s=set()
    for _ in range(n+m):
        s.add(int(input()))
    print(n+m-len(s))

