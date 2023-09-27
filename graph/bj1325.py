#!/usr/bin/env python

import sys
input= sys.stdin.readline
from collections import deque

n,m=map(int,input().split())
li=[[]*n for _ in range(n)]
ans=[]

for _ in range(m):
    a,b=map(int,input().split())
    li[b-1].append(a-1)

def bfs(v):
    q=deque()
    q.append(v)
    cnt=0

    visit=[False]*n
    visit[v]=True

    while q:
        x = q.popleft()
        for next in li[x]:
            if not visit[next]:
                visit[next]=True
                q.append(next)
                cnt+=1
    ans.append(cnt)

for i in range(len(li)):
    bfs(i)

maxx=max(ans)
for i in range(len(ans)):
    if ans[i]==maxx:
        print(i+1,end =' ')
