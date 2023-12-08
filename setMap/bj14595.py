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
        for i in range(a+1,b+1):
            parent[i]=a
    else:
        for i in range(b+1,a+1):
            parent[i]=b

v=int(input())
e=int(input())
parent=[i for i in range(v+1)]

for _ in range(e):
    a,b=map(int,input().split())
    union(a,b)

for i in range(1,v+1):
    find(i)

parent=set(parent)
print(len(parent)-1)

