#!/usr/bin/env python

import sys
input= sys.stdin.readline

n=int(input())
parent=[i for i in range(n+1)]

def find(x):
    if x!=parent[x]:
        parent[x]=find(parent[x])
        return parent[x]
    else:
        return x

def union(a,b):
    a,b=find(a),find(b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

for _ in range(int(input())):
    x,y=map(int,input().split())
    union(x,y)

for i in range(1,n+1):
    find(i)

s=set(parent[1:])
print(len(s)-1)
