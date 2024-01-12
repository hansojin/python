#!/usr/bin/env python

import sys
input= sys.stdin.readline

n,m=map(int,input().split())
li=[[0]*n for _ in range(m)]
one=list(map(int,input().split()))

for i in range(m):
    for j in range(one[i]):
        li[i][j]=1

def rotate(li):
    new= [[0]*m for _ in range(n)]
    for i in range(m):
        for j in range(n):
            new[n-j-1][i]=li[i][j]
    return new

li=rotate(li)

cnt=0
for i in li:
    tot=sum(i)
    if tot<2:
        continue
    istr=''.join(str(s) for s in i)
    cnt+=(istr.rindex('1')-istr.index('1'))+1-tot
print(cnt)
    
