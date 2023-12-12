#!/usr/bin/env python

import sys
input= sys.stdin.readline
mod=1000000007
def find(x):
    px=parent[x]
    if x!=px:
        return find(px)
    return x
def union(a,b):
    a,b=find(a),find(b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

n,m=map(int,input().split())
parent=[i for i in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    union(a,b)

d=dict()
for i in range(n+1):
    k=find(i)
    if k not in d:
        d[k]=1
    else:
        d[k]+=1
ans=1
for i in d.values():
    ans*=i

print(ans%mod)
    
