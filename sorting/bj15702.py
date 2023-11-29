#!/usr/bin/env python

import sys
input= sys.stdin.readline

n,m=map(int,input().split())
li=list(map(int,input().split()))
score=[[0,0] for _ in range(m)]
for i in range(m):
    tmp=input().split()
    score[i][0]=int(tmp[0])
    for j in range(1,n+1):
        if tmp[j]=="O":
            score[i][1]+=li[j-1]
score.sort(key=lambda x:(-x[1],x[0]))
print(score[0][0],score[0][1])
