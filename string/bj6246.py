#!/usr/bin/env python

import sys
input= sys.stdin.readline

n,m=map(int,input().split())
li=[0 for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    for i in range(a,n+1,b):
        li[i]=1
print(li.count(0)-1)

