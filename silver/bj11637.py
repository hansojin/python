#!/usr/bin/env python

import sys
input= sys.stdin.readline

for _ in range(int(input())):
    li=[]
    for _ in range(int(input())):
        li.append(int(input()))
    maxVote= max(li)
    maxIdx = li.index(max(li))+1
    li.sort()
    if li[-1]==li[-2]:
        print('no winner')
    else:
        if sum(li)//2<maxVote:
            print('majority winner',end=' ')
            print(maxIdx)
        else:
            print('minority winner',end=' ')
            print(maxIdx)

