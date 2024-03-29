#!/usr/bin/env python

import sys
input= sys.stdin.readline
import heapq

def find(x):
    if x!=parent[x]:
        return find(parent[x])
    return x

def union(a,b):
    a,b=find(a),find(b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

p,w=map(int,input().split())
c,v=map(int,input().split())
parent=list(range(p))

pq = []

for i in range(w):
    n, e, width = map(int, input().split())
    heapq.heappush(pq, (-width, n, e))

while pq:
    cost, start, end = heapq.heappop(pq)
    cost = -cost
    union(start, end)

    if find(c) == find(v):
        result = cost
        break

print(result)
