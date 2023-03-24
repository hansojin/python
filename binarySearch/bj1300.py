#!/usr/bin/env python

n=int(input())
k=int(input())

#a=[[0 for _ in range(1,n+1)] for _ in range(1,n+1)]
b=[]
for i in range(1,n+1):
    for j in range(1,n+1):
        #a[i][j]=i*j
        b.append(i*j)
b.sort()
print(b[k])
