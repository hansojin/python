#!/usr/bin/env python

for i in range(int(input())):
    li=[]
    n=int(input())
    for k in range(2):
        li.append(list(map(int,input().split())))
    for j in range(1,n):
        if j==1:
            li[0][j]+=li[1][j-1]
            li[1][j]+=li[0][j-1]
        else:
            li[0][j]+=max(li[1][j-1],li[1][j-2])
            li[1][j]+=max(li[0][j-1],li[0][j-2])
    print(max(li[0][n-1],li[1][n-1]))

