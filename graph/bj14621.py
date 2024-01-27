#!/usr/bin/env python

import sys
input= sys.stdin.readline

def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]

def union(a,b):
    a,b=find(a),find(b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

n,m=map(int,input().split())
parent=[0]*(n+1)
gender=list(map(str,input().split()))
edges=[]
res,cnt=0,0

for i in range(1,n+1):
    parent[i]=i

for _ in range(m):
    a,b,c=map(int,input().split())
    edges.append((c,a,b))

edges.sort()

for e in edges:
    c,i,j=e
    if gender[i-1]!=gender[j-1]:
        if find(i)!=find(j):
            union(i,j)
            res+=c
            cnt+=1
if cnt!=n-1:
    print(-1)
else:
    print(res)

