#!/usr/bin/env python

import sys
input= sys.stdin.readline

cnt=0
tmp=set()
n=int(input())
for i in range(n):
    enter=input().strip()
    if enter=="ENTER":
        cnt+=len(tmp)
        tmp=set()
    else:
        tmp.add(enter)
    if i==n-1:
        cnt+=len(tmp)
print(cnt)
