#!/usr/bin/env python

cases=int(input())
for case in range(cases):
    n=int(input())
    li=[[0]*n for _ in range(n)]
    for i in range(n):
        li[i][0]=1
        li[i][i]=1
    for i in range(n):
        for j in range(i):
            if li[i][j]==0:
                li[i][j]=li[i-1][j]+li[i-1][j-1]
    print(f'#{case+1}')
    for i in li:
        for j in i:
            if j!=0:
                print(j,end=' ')
        print('')


