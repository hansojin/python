#!/usr/bin/env python

n,m=map(int,input().split())
li=[[0]*n for _ in range(n)]
for i in range(n):
    li[i][0]=1
    li[i][i]=1
for i in range(n):
    for j in range(i):
        if li[i][j]==0:
            li[i][j]=li[i-1][j]+li[i-1][j-1]
print(li[n-1][m-1])
        
