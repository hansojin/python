#!/usr/bin/env python

import sys
input= sys.stdin.readline
from collections import deque

f,s,g,u,d=map(int,input().split())
graph=[[] for _ in range(f+1)]

q=deque([s])
dist=[0]*(f+1)

while q:
    x=q.popleft()
    if x==g:
        print(dist[x])
        break

    for nxt in (x+u, x-d):
        if nxt==x:
            continue
        if 1<=nxt<=f and not dist[nxt]:
            dist[nxt]=dist[x]+1
            q.append(nxt)
else:
    print("use the stairs")
