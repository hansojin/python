#!/usr/bin/env python

n=int(input())
li=[]

for _ in range(n):
    li.append(list(map(int,input().split())))

for i in range(1,n):
    for j in range(0,3):
        if j==0:
            li[i][j]=li[i][j]+min(li[i-1][1],li[i-1][2])
        elif j==1:
            li[i][j]=li[i][j]+min(li[i-1][0],li[i-1][2])
        else:
            li[i][j]=li[i][j]+min(li[i-1][1],li[i-1][0])
print(min(li[n-1]))


