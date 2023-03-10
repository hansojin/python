#!/usr/bin/env python

import sys
input = sys.stdin.readline

n,m=map(int,input().split())
a=list(map(int,input().split()))

cnt=0
s=e=0
subsum=a[s]

while True:
    if e<n-1:
        e+=1
        subsum+=a[e]
        if subsum%m==0:
            cnt+=1
    else:
        s+=1
        if s==n-1:
            break
        subsum=a[s]
        if subsum%m==0:
            cnt+=1
        e=s

print(cnt)



