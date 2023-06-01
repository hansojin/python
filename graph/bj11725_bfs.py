#!/usr/bin/env python

from collections import deque
import sys
input= sys.stdin.readline

n=int(input())
visit=[0]*(n+1)
ans=[0]*(n+1)
e=[[]for _ in range(n+1)]

for i in range(n-1):
    a,b=map(int,input().split())
    e[a].append(b)
    e[b].append(a)

def bfs(e,v,visit):
    q=deque([v])
    visit[v]=1
    while q:
        x=q.popleft()
        for i in e[x]:
            if not visit[i]:
                ans[i]=x
                q.append(i)
                visit[i]=1
bfs(e,1,visit)

for i in range(2,n+1):
    print(ans[i])
