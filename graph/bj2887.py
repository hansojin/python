#!/usr/bin/env python

import sys
input= sys.stdin.readline

def find(x,parent):
    if x!=parent[x]:
        parent[x]=find(parent[x],parent)
    return parent[x]

def union(a,b,parent):
    a=find(a,parent)
    b=find(b,parent)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

n=int(input())
c=[]
for i in range(n):
    x,y,z=map(int,input().split())
    c.append((x,y,z,i))

e=[]
for i in range(3):
    c.sort(key=lambda x:x[i])
    for j in range(1,n):
        e.append((abs(c[j-1][i]-c[j][i]), c[j-1][3],c[j][3]))
parent=[i for i in range(n)]
ans=0
e.sort()

for i in range(len(e)):
    if find(e[i][1],parent)!=find(e[i][2],parent):
        union(e[i][1],e[i][2],parent)
        ans+=e[i][0]
print(ans)
