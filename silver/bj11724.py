#!/usr/bin/env python

import sys
input= sys.stdin.readline

n,m=map(int,input().split())
parent=[i for i in range(n+1)]

def find(x):
    if x==parent[x]:
        return x
    parent[x]=find(parent[x])
    return parent[x]
def union(a,b):
    a,b=find(a),find(b)
    parent[b]=a

for _ in range(m):
    a,b=map(int,input().split())
    union(a,b)

for i in range(n+1):
    find(i)

s=set()
for i in parent:
    s.add(i)
print(len(s)-1)
