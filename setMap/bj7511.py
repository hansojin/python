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

for i in range(int(input())):
    print(f'Scenario {i+1}:')
    v=int(input())
    parent=[i for i in range(v+1)]
    e=int(input())
    for i in range(e):
        a,b=map(int,input().split())
        union(a,b)
    for i in range(1,v+1):
        find(i)
    for _ in range(int(input())):
        a,b=map(int,input().split())
        if parent[a]==parent[b]:
            print(1)
        else:
            print(0)
    print()
