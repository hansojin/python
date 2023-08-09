#!/usr/bin/env python

import sys
input= sys.stdin.readline

n,m,k=map(int,input().split())
li=[[0]*m for _ in range(n)]

one = [0 for _ in range(n)]
two = [0 for _ in range(m)]
for _ in range(k):
    num, r,v = map(int,input().split())

    if num==1:
        one[r-1]+=v
            
    else:
        two[r-1]+=v

for i in range(n):
    for j in range(m):
        li[i][j]+=one[i]

for j in range(m):
    for i in range(n):
        li[i][j]+=two[j]


for i in li:
    for j in i:
        print(j, end=' ')
    print()
