#!/usr/bin/env python

import sys
input= sys.stdin.readline

def find(x):
    if parent[x]<0:
        return x
    else:
        y=find(parent[x])
        parent[x]=y
        return y

def union(a,b):
    a,b=find(a),find(b)
    if a==b:
        return
    if parent[a]<parent[b]:
        x,y=a,b
    else:
        x,y=b,a
    parent[x]+=parent[y]
    parent[y]=x

n=int(input())
parent=[-1 for i in range(1000001)]

for _ in range(n):
    order=input().split()
    if order[0]=='I':
        a,b=int(order[1]),int(order[2])
        union(a,b)
    else:
        print(parent[find(int(order[1]))]*-1)


