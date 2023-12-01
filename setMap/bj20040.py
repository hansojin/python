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
    if a<b:
        p[b]=a
    else:
        p[a]=b

v,e=map(int,input().split())
parent=[i for i in range(v+1)]

cycle=False

for i in range(e):
    a,b=map(int,input().split())
    if findP(parent,a)==findP(parent,b):
        cycle=True
        ans=i+1
        break
    else:
        unionP(parent,a,b)

if cycle:
    print(ans)
else:
    print(0)
