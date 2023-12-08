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

cnt=1
while True:
    n=int(input())
    if n==0:
        break
    parent=[i for i in range(n+1)]
    idx={}
    num=0
    for _ in range(n):
        a,b=input().split()
        if a not in idx:
            idx[a]=num
            num+=1
        if b not in idx:
            idx[b]=num
            num+=1
        union(idx[a],idx[b])

    print(f'{cnt} {len(set(parent))-1}')
    cnt+=1
    
