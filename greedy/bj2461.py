#!/usr/bin/env python

import sys
input= sys.stdin.readline
from collections import deque
import heapq

n,m=map(int,input().split())
li=[deque(sorted(list(map(int,input().split())))) for _ in range(n)]
heap=[]

maxx=-1
minn=10e9
for i in range(len(li)):
    v=li[i].popleft()
    maxx=max(maxx,v)
    minn=min(minn,v)
    heapq.heappush(heap,[v,i])

diff=maxx-minn
while heap:
    prev,now = heapq.heappop(heap)
    if not li[now]:
        break
    new=li[now].popleft()
    heapq.heappush(heap,[new,now])
    if maxx<new:
        maxx=new
    minn=heap[0][0]
    diff=min(diff,maxx-minn)
print(diff)
