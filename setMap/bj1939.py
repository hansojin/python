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
    parent[max(a,b)]=min(a,b)

def check(a,b):
    return find(a)==find(b)

n,m=map(int,input().split())
parent=[i for i in range(n+1)]
graph=[]

for _ in range(m):
    a,b,c=map(int,input().split())
    graph.append([c,a,b])

s,e=map(int,input().split())

graph.sort(reverse=True)
for i in graph:
    c,a,b=i[0],i[1],i[2]
    union(a,b)
    if check(s,e):
        print(c)
        break
