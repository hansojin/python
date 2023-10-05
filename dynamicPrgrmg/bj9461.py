#!/usr/bin/env python

tri=[0]*101



tri[1]=1
tri[2]=1
tri[3]=1
tri[4]=2


for i in range(5,101):
    tri[i]=tri[i-1]+tri[i-5]

n=int(input())
for _ in range(n):
    print(tri[int(input())])
