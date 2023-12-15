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

n,m=map(int,input().split())
parent=[i for i in range(n+1)]
li=[0]
for _ in range(n):
    li.append(int(input()))

for _ in range(m):
    a,b=map(int,input().split())
    aa,bb=find(a),find(b)
    if aa!=bb: 
        union(a,b)
        li[find(a)]=li[aa]+li[bb]
    print(li[find(a)])
