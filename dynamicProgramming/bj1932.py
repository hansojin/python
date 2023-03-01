#!/usr/bin/env python

n=int(input())
li=[[[0] for _ in range(n)] for _ in range(n)]
for i in range(n):
    li[i]=list(map(int,input().split()))
j=0
for i in range(1,n):

    li[i][j]=max(li[i][j]+li[i-1][j],li[i][j]+li[i-1][j-1])
print(max(li))
