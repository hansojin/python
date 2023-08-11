#!/usr/bin/env python

import sys, heapq
input= sys.stdin.readline

n=int(input())
m=int(input())
graph=[[] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

s,e = map(int,input().split())

near = [s]*(n+1)
dist = [1e9]*(n+1)

q=[(0,s)]
while q:
    d,now = heapq.heappop(q)
    if d>dist[now]:
        continue

    for nxt, nxtD in graph[now]:
        cost = nxtD + d
        if cost < dist[nxt]:
            dist[nxt], near[nxt] = cost,now
            heapq.heappush(q,(cost,nxt))
ans=[]
tmp=e

while tmp!=s :
    ans.append(str(tmp))
    tmp=near[tmp]

ans.append(str(s))
ans.reverse()

print(dist[e])
print(len(ans))
print(*ans)
