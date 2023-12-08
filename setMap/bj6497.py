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

while True:
    v,e=map(int,input().split())
    if v==e==0:
        break
    parent=[i for i in range(v)]
    edges=[]
    cost,total=0,0
    
    for _ in range(e):
        a,b,c=map(int,input().split())
        total+=c
        edges.append((c,a,b))

    edges.sort()
    for edge in edges:
        c,a,b=edge
        if find(a)!=find(b):
            union(a,b)
            cost+=c
    print(total-cost)

