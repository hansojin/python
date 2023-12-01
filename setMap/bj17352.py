#!/usr/bin/env python

import sys
input= sys.stdin.readline

def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]

def union(a,b):
    a=find(a)
    b=find(b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

v=int(input())
parent=[i for i in range(v+1)]

for _ in range(v-2):
    a,b=map(int,input().split())
    union(a,b)
for i in range(1,v+1):
    find(i)

s=set()
for i in range(1,v+1):
    s.add(parent[i])

print(*s)
