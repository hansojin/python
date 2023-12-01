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
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

v,e=map(int,input().split())
parent=[i for i in range(v+1)]

for i in range(e):
    a,b=map(int,input().split())
    union(a,b)
for i in range(1,v+1):
    find(i)
cnt=0
li=list(map(int,input().split()))
for i in range(v-1):
    if parent[li[i]]!=parent[li[i+1]]:
        cnt+=1
print(cnt)
