#!/usr/bin/env python

import sys
input= sys.stdin.readline

def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]

def union(a,b):
    a,b=find(a),find(b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

n,m,t=map(int,input().split())
parent = [i for i in range(n+1)]
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()
lines, result = 0, 0
for edge in edges:
    cost, a, b = edge
    if find(a) != find(b):
        union(a, b)
        result += cost
    if lines == n-1:
        break
print(result+((n-2)*(n-1)//2)*t)
