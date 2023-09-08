#!/usr/bin/env python

from collections import deque

n,k=map(int,input().split())
q = deque()
t=[0]*100001
path = [0]*100001

def move(x):
    arr=[]
    tmp=x
    for _ in range(t[x]+1):
        arr.append(tmp)
        tmp=path[tmp]
    print(' '.join(map(str,arr[::-1])))


def bfs():
    cnt=0
    q.append(n)
    while q:
        now = q.popleft()
        if now ==k:
            print(t[k])
            move(k)
            break

        for nxt in (now-1,now+1,now*2):
            if 0<=nxt<100001 and (t[nxt]==0 or t[nxt]==t[now]+1):
                t[nxt]=t[now]+1
                q.append(nxt)
                path[nxt]=now
bfs()

