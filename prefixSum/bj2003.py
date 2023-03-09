#!/usr/bin/env python

import sys
input = sys.stdin.readline

n,m=map(int,input().split())
a=list(map(int,input().split()))

s=e=0
subsum=a[0]
cnt=0

while True:
    if subsum<m:
        e+=1
        if e>=n:
            break
        subsum+=a[e]

    elif subsum==m:
        cnt+=1
        subsum-=a[s]
        s+=1
    else:
        subsum-=a[s]
        s+=1
print(cnt)
