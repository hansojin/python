#!/usr/bin/env python

import sys
input= sys.stdin.readline

li=[0]*10
visit=[0]*10
cnt=0

for _ in range(int(input())):
    n,m=map(int,input().split())
    if visit[n]:
        if li[n]!=m:
            cnt+=1
            li[n]=m
    else:
        visit[n]=1
        li[n]=m
print(cnt)
