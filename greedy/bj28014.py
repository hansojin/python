#!/usr/bin/env python

import sys
input= sys.stdin.readline

ans=1
n=int(input())
li=list(map(int,input().split()))
for i in range(n-1):
    if li[i]<=li[i+1]:
        ans+=1
print(ans)
