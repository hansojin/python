#!/usr/bin/env python

import sys
input= sys.stdin.readline
import math 

def rotate(li):
    n=len(li)
    res=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            res[n-j-1][i]=li[i][j]
    return res
    
for _ in range(int(input())):
    word=input().rstrip()
    line= int(math.sqrt(len(word)))
    li=[[0]*(line) for _ in range(line)]
    idx=0
    for i in range(line):
        for j in range(line):
            li[i][j]=word[idx]
            idx+=1
    ret = rotate(li)
    for i in ret:
        for j in i:
            print(j,end='')
    print()

    
