#!/usr/bin/env python

import sys
input= sys.stdin.readline

def find(x):
    if x==parent[x]:
        return x
    parent[x]=find(parent[x])
    return parent[x]

def union(a,b):
    a,b=find(a),find(b)
    parent[b]=a

g=int(input())
p=int(input())
li=[int(input()) for _ in range(p)]

parent=[i for i in range(g+1)]
cnt=0
for i in li:
    tmp=find(i)
    if tmp==0:
        break
    union(tmp-1,tmp)
    cnt+=1
print(cnt)
