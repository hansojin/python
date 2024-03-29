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

n=int(input())
m=int(input())
e=[[] for _ in range(n+1)]
parent=[i for i in range(n+1)]

for _ in range(m):
    rel,a,b=input().split()
    a,b=int(a),int(b)
    if rel=='F':
        union(a,b)
    else:
        e[a].append(b)
        e[b].append(a)

for i in range(1,n+1):
    for e1 in range(len(e[i])):
        for e2 in range(e1+1,len(e[i])):
            union(e[i][e1],e[i][e2])
ans=set()
for i in range(1,n+1):
    ans.add(find(i))
print(len(ans))
