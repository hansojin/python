#!/usr/bin/env python

import sys
input = sys.stdin.readline

n,m=map(int,input().split())
li=list(map(int,input().split()))
a=[0]
tmp=0
for i in li:
    tmp+=i
    a.append(tmp)
cnt=0
for i in range(n+1):
    for j in range(i+1,n+1):
        if (a[j]-a[i])%m==0:
            cnt+=1
print(cnt)



