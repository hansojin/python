#!/usr/bin/env python

import sys
input= sys.stdin.readline

n=int(input())
li=sorted(list(map(int,input().split())))
se=[]
cnt,tmp=1,li[0]
for i in range(n-1):
    if li[i+1]>tmp:
        cnt+=1
        tmp=li[i+1]
    else:
        se.append(li[i+1])

if se:
    cnt+=1
    tmp=se[0]
    for i in range(len(se)-1):
        if se[i+1]>tmp:
            cnt+=1
            tmp=se[i+1]
print(cnt)
