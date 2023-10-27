#!/usr/bin/env python

import sys
input= sys.stdin.readline

v,e=map(int,input().split())
vroot = [i for i in range(v+1)]
eli = []

for _ in range(e):
    eli.append(list(map(int,input().split())))

eli.sort(key=lambda x : x[2])

def find(x):
    if x!=vroot[x]:
        vroot[x]=find(vroot[x])
    return vroot[x]

ans=0
for s,e,w in eli:
    sroot=find(s)
    eroot=find(e)
    if sroot!=eroot:
        if sroot>eroot:
            vroot[sroot]=eroot
        else:
            vroot[eroot]=sroot
        ans+=w
print(ans)
