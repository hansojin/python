#!/usr/bin/env python

import sys
input= sys.stdin.readline

li=[[0]*101 for _ in range(101)]

for _ in range(4):
    a,b,c,d=map(int,input().split())
    for i in range(a,c):
        for j in range(b,d):
            li[i][j]=1

summ=0
for i in range(101):
    summ+=sum(li[i])
print(summ)
