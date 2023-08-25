#!/usr/bin/env python

import sys
input= sys.stdin.readline
from collections import deque

n,l=map(int,input().split())
li=list(map(int,input().split()))
dq=deque([])

for i in range(n):
    if dq and dq[0][0]<=i-l:
        dq.popleft()
    while len(dq)>=1 and li[i]<dq[-1][1]:
        dq.pop()
    dq.append((i,li[i]))
    print(dq[0][1],end=" ")
