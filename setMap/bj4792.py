#!/usr/bin/env python

import sys
input= sys.stdin.readline
import heapq

def find(x):
    if parent[x]==x:
        return x
    else:
        parent[x]=find(parent[x])
        return parent[x]

def union(a,b):
    a,b=find(a),find(b)
    if a==b:
        return False
    else:
        parent[b]=a
        return True

def krusk(pq):
    ed, blue = 0,0
    while pq:
        c,n1,n2,br = heapq.heappop(pq)
        if union(n1,n2):
            if br=='B':
                blue+=1
            ed+=1
            if ed==n-1:
                return blue

while True:
    n,m,k=map(int,input().split())
    if n==m==k==0:
        break

    red,blue=[],[]

    for i in range(m):
        c,s,e=input().split()
        s,e=int(s),int(e)
        if c=='R':
            heapq.heappush(red,[0,s,e,c])
            heapq.heappush(blue,[1,s,e,c])
        else:
            heapq.heappush(red,[1,s,e,c])
            heapq.heappush(blue,[0,s,e,c])
    parent=[i for i in range(n+1)]
    minb = krusk(red)
    parent=[i for i in range(n+1)]
    maxb = krusk(blue)

    if minb<=k and k<=maxb:
        print(1)
    else:
        print(0)


