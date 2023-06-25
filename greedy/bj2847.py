#!/usr/bin/env python

import sys
input= sys.stdin.readline

li=[]
n=int(input())
for _ in range(n):
    li.append(int(input()))

ans=0
rev=li[::-1]
for i in range(n-1):
    if rev[i]<=rev[i+1]:
        m=rev[i+1]-rev[i]+1
        ans+=m
        rev[i+1]-=m
print(ans)
    
