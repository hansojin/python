#!/usr/bin/env python

cases=int(input())
for case in range(cases):
    
    n=int(input())
    li=[[0]*n for _ in range(n)]

    row,col=0,-1
    cnt,trans=1,1

    while n>0:
        for i in range(n):
            col+=trans
            li[row][col]=cnt
            cnt+=1
        n-=1
        for j in range(n):
            row+=trans
            li[row][col]=cnt
            cnt+=1
        trans*=-1

    print(f'#{case+1}')
    for i in li:
        for j in i:
            print(j,end=' ')
        print('')

