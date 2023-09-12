#!/usr/bin/env python

import sys
input= sys.stdin.readline

li=[]
n,m=map(int,input().split())
for _ in range(n):
    li.append(list(map(int,input().split())))
k=int(input())

add=[ 0 for _ in range(m)]
for j in range(m):
    for i in range(n):
        add[j]+=li[i][j]

maxx=[]
summ=sum(add[0:k])
maxx.append(summ)

for i in range(m-k):
    summ-=add[i] 
    summ+=add[i+k]
    maxx.append(summ)

print(max(maxx))

