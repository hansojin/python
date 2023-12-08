#!/usr/bin/env python

import sys
input= sys.stdin.readline

def find(x):
    if parent[x]!=x:
        return find(parent[x])
    return x

def union(a,b):
    a,b=find(a),find(b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

for _ in range(int(input())):
    n=int(input())
    m=int(input())
    parent=[i for i in range(n+1)]
    cycle=False

    for _ in range(m):
        a,b=map(int,input().split())
        if find(a)==find(b):
            cycle=True
        else:
            union(a,b)
    if cycle:
        print("graph")
    else:
        print("tree")

