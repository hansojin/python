#!/usr/bin/env python

import sys
input= sys.stdin.readline

n=int(input())
a=[]
b=[[1]*n for _ in range(n)]
c=0

for i in range(n):
    a.append(list(map(int,input().split())))

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i==j or j==k or i==k:
                continue
            if a[i][j] == a[i][k]+a[k][j]:
                b[i][j]=0
            elif a[i][j] > a[i][k]+a[k][j]:
                c=-1
if c!=-1:
    for i in range(n):
        for j in range(n):
            if b[i][j]==1:
                c+=a[i][j]
print(c//2)

