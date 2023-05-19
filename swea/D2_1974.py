#!/usr/bin/env python

import sys
input= sys.stdin.readline

cases=int(input())
for case in range(cases):
    li=[]
    ret=1
    for _ in range(9):
        li.append(list(map(int,input().split())))

    for i in range(9):
        # print(li[i])
        col=sorted(li[i])
        if col != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            ret=0
            break
        tmp=[]
        for j in range(9):
            tmp.append(li[j][i])
        # print(tmp)
        tmp.sort()
        # print(tmp)
        if tmp != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            ret=0
            break

    for i in range(0,7,3):
        for j in range(0,7,3):
            square=[]
            for l in range(i,i+3):
                for k in range(j,j+3):
                    square.append(li[l][k])
            square.sort()
            # print(square)
            if square!=[1,2,3,4,5,6,7,8,9]:
                ret=0
                break



    print(f'#{case+1} {ret}')

