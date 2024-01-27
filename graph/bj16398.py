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

n=int(input())
parent=[0]*n
li=[list(map(int,input().split())) for _ in range(n)]
edges=[]
res=0

for i in range(n):
    parent[i]=i

for i in range(n):
    for j in range(n):
        if i!=j:
            edges.append((li[i][j],i,j))

edges.sort()

for e in edges:
    c,i,j=e
    if find(i)!=find(j):
        union(i,j)
        res+=c

print(res)
