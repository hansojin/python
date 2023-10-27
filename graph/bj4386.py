#!/usr/bin/env python

import sys
input= sys.stdin.readline

v=int(input())
e=v*(v-1)//2
vroot = [i for i in range(v)]
eli = []
star=[]
for _ in range(v):
    star.append(list(map(float,input().split())))

def cost(A,B):
    ax,ay=A[0],A[1]
    bx,by=B[0],B[1]
    tmp = pow((ax-bx),2) + pow((ay-by),2)
    return pow(tmp,0.5)

for i in range(0,v):
    for j in range(i+1,v):
        w=cost(star[i],star[j])
        eli.append([i,j,w])

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

