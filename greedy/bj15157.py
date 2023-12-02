#!/usr/bin/env python

import sys
input= sys.stdin.readline

n=int(input())
li=list(map(int,input().split()))
tmp=li[0]
for i in range(n):
    if i==0:
        print(li[0],end=' ')
    else:
        tmp=min(tmp+1,li[i])
        print(tmp,end=' ')

