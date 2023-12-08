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

n,m=map(int,input().split())
parent=[i for i in range(n+1)]
cnt,link=0,0

for _ in range(m):
    x,y=map(int,input().split())
    if find(x)==find(y):
        cnt+=1
    union(x,y)


for i in range(1,n):
    if find(i)!=find(i+1):
        union(i,i+1)
        link+=1

print(cnt+link)


