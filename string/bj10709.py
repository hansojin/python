#!/usr/bin/env python

import sys
input= sys.stdin.readline

n,m=map(int,input().split())
li=[list(input()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if j==0:
            if li[i][j]=='c':
                li[i][j]=0
            else:
                li[i][j]=-1
        else:
            if li[i][j-1]!=-1:
                if li[i][j]=='c':
                    li[i][j]=0
                else:
                    li[i][j]=li[i][j-1]+1
            else:
                if li[i][j]=='c':
                    li[i][j]=0
                else:
                    li[i][j]=-1
for i in range(n):
    for j in range(m):
        print(li[i][j], end= ' ' )
    print()
