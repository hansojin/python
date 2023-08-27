#!/usr/bin/env python

import sys
input= sys.stdin.readline

n,m=map(int,input().split())
li=[]
for _ in range(n):
    li.append(int(input()))

for _ in range(m):
    a,b=map(int,input().split())
    print(min(li[a-1:b]),max(li[a-1:b]))

