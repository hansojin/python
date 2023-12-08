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


v,e,city=map(int,input().split())
li=list(map(int,input().split()))

parent=[0]*(v+1)
for i in range(1,v+1):
    if i in li:
        continue
    parent[i]=i

edges=[]
ans=0
for _ in range(e):
    a,b,c=map(int,input().split())
    edges.append((c,a,b))
edges.sort()
for edge in edges:
    c,a,b=edge
    if find(a)!=find(b):
        union(a,b)
        ans+=c
print(ans)
        

