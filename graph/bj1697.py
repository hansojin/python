#!/usr/bin/env python

from collections import deque

n,k=map(int,input().split())
q = deque()
t=[0]*100001

def bfs():
    q.append(n)
    while q:
        now = q.popleft()
        if now ==k:
            print(t[now])
            return
        for nxt in (now-1,now+1,now*2):
            if 0<=nxt<100001 and t[nxt]==0:
                t[nxt]=t[now]+1
                q.append(nxt)
bfs()
