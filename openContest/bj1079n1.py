#!/usr/bin/env python

import sys
input= sys.stdin.readline

n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

cnt=0
for i in range(n):
    if b[i]-a[i]>=0:
        cnt+=1
print(cnt)
