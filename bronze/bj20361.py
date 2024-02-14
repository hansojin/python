#!/usr/bin/env python

import sys
input= sys.stdin.readline

n,x,k=map(int,input().split())
li=[0]*(n+1)
li[x]=1
for _ in range(k):
    a,b=map(int,input().split())
    li[a],li[b]=li[b],li[a]
print(li.index(1))
