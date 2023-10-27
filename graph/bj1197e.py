#!/usr/bin/env python

import sys
input= sys.stdin.readline
import heapq

v,e=map(int,input().split())
visit=[False]*(v+1)
eli=[[] for _ in range(v+1)]
heap = [[0,1]]

for _ in range(e):
    s,e,w=map(int,input().split())
    eli[s].append([w,e])
    eli[e].append([w,s])

ans,cnt=0,0
while heap:
    if cnt==v:
        break
    w,s=heapq.heappop(heap)
    if not visit[s]:
        visit[s]=True
        ans+=w
        cnt+=1
        for i in eli[s]:
            heapq.heappush(heap,i)
print(ans)
