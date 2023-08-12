#!/usr/bin/env python

import sys
input= sys.stdin.readline
from collections import deque

n=int(input())
li=[list(map(int,input().split())) for _ in range(n)]

for _ in range(int(input())):
    option = input().split()
    if int(option[0])==2:
        tmp=[[0]*n for _ in range(n)]
        for c in range(n):
            for r in range(n):
                tmp[c][r]=li[n-1-r][c]
        li=tmp
    elif int(option[0])==1:
        trgt = int(option[1])-1
        tmp= li[trgt]
        tmp= deque(tmp)
        tmp.rotate(1)
        li[trgt]=tmp

for i in range(n):
    for j in range(n):
        print(li[i][j],end =' ')
    print()
