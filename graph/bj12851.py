#!/usr/bin/env python

from collections import deque

n,k=map(int,input().split())
q = deque()
t=[-1]*100001
t[n]=0
def bfs():
    q.append(n)
    while q:
        s = q.popleft()
        if s ==k:
            print(t[k])
            break

        for w in (2*s,s-1,s+1):
            if 0<=w<100001 and t[w]==-1:
                if w==2*s:
                    t[w]=t[s]
                    q.appendleft(w)
                else:
                    t[w]=t[s]+1
                    q.append(w)

bfs()


