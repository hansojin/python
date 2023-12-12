#!/usr/bin/env python

import sys
input= sys.stdin.readline

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

n,m,k=map(int,input().split())
parent=[i for i in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    union(a,b)

for _ in range(k):
    a,b=map(int,input().split())
    if find(a)==find(b):
        print("Y")
    else:
        print("N")
