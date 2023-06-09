#!/usr/bin/env python

import sys
input= sys.stdin.readline

n=int(input())
li=list(map(int,input().split()))
prefix=[0]*(n+1)
for i in range(n):
    prefix[i+1]=li[i]+prefix[i]

for _ in range(int(input())):
    a,b=map(int,input().split())
    print(prefix[b]-prefix[a-1])

