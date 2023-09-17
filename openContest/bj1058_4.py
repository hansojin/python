#!/usr/bin/env python

import sys
input= sys.stdin.readline

s,n,m=map(int,input().split())
oper=[]
for _ in range(n+m):
    oper.append(int(input()))
now=0
for op in oper:
    if op==1:
        if now<s:
            now+=1
        else:
            s*=2
    else:
        if now==0:
            continue
        else:
            now-=1
print(s)
