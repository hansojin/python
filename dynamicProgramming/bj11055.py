#!/usr/bin/env python

import sys
input= sys.stdin.readline

n=int(input())
li=list(map(int,input().split()))
arr=[1]*n
arr[0]=li[0]
for i in range(1,n):
    for j in range(i):
        if li[j]<li[i]:
            arr[i]=max(arr[i],arr[j]+li[i])
        else:
            arr[i]=max(arr[i],li[i])
print(max(arr))

