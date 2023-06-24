#!/usr/bin/env python

import sys
input= sys.stdin.readline

n=int(input())
li=list(map(int,input().split()))
arr=[1]*(n+1)

for i in range(1,n):
    for j in range(i):
        if li[j]>li[i]:
            arr[i]=max(arr[i],arr[j]+1)

print(max(arr))
