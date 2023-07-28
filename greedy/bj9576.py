#!/usr/bin/env python

#Bipartite matching
import sys
input= sys.stdin.readline
from collections import deque

for _ in range(int(input())):
    n,m=map(int,input().split())
    book = [False]*(n+1)

    req=[]
    for _ in range(m):
        req.append(list(map(int,input().split())))
    req.sort(key=lambda x:x[1])

    cnt=0
    while req:
        a,b=req.pop(0)
        
        for i in range(a,b+1):
            if not book[i]:
                cnt+=1
                book[i]=True
                break
    print(cnt)
