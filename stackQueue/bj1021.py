#!/usr/bin/env python

import sys
input= sys.stdin.readline

from collections import deque

n,m=map(int,input().split())
dq=deque()
for i in range(1,n+1):
    dq.append(i)
li = list(map(int,input().split()))

cnt=0
for i in li:
    while True:
        if dq[0]==i:
            dq.popleft()
            break
        else:
            if dq.index(i) <= len(dq)//2:
                dq.rotate(-1)
                cnt+=1
            else:
                dq.rotate(1)
                cnt+=1
print(cnt)
