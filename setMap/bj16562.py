#!/usr/bin/env python

import sys
input= sys.stdin.readline

def findP(p,x):
    if p[x]!=x:
        p[x]=findP(p,p[x])
    return p[x]

def unionP(p,a,b):
    a=findP(p,a)
    b=findP(p,b)
    if a!=b:
        if li[a]<=li[b]:
            p[b]=a
    
        else:
            p[a]=b

v,e,k=map(int,input().split())
parent=[i for i in range(v+1)]
li=[0]+list(map(int,input().split()))

for i in range(e):
    a,b=map(int,input().split())
    unionP(parent,a,b)

ans=0
for idx,root in enumerate(parent):
    if idx==root:
        ans+=li[idx]

if ans<=k:
    print(ans)
else:
    print("Oh no")
