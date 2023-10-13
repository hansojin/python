#!/usr/bin/env python

import sys
input= sys.stdin.readline

n=int(input())
m=int(input())
li = [list(map(int,input().split())) for _ in range(n)]

parent = [i for i in range(n+1)]

def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a<b:
        parent[a]=b
    else:
        parent[b]=a

for i in range(n):
    for j in range(i):
        if li[i][j]==1:
            union(i+1,j+1)

course = list(map(int,input().split()))

flag = True

for i in range(len(course)-1):
    if find(course[i])==find(course[i+1]):
        continue
    else:
        flag=False
        break
if flag:
    print("YES")
else:
    print("NO")
