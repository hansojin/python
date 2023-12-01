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
    if frq[a]>=frq[b]:
        parent[b]=a
    else:
        parent[a]=b

v=int(input())
e=int(input())
parent=[i for i in range(v+1)]
frq = [0 for i in range(v+1)]
tmp=[]
for i in range(e):
    a,b=map(int,input().split())
    tmp.append([a,b])
    frq[a]+=1
    frq[b]+=1

for a,b in tmp:
    union(a,b)

for i in range(1,v+1):
    find(i)
s=set()
for i  in range(1,v+1):
    s.add(parent[i])
print(len(s))
s=list(s)
for i in sorted(s) :
    print(i)
