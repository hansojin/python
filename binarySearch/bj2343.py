#!/usr/bin/env python

import sys
input= sys.stdin.readline

n,m=map(int,input().split())
li=list(map(int,input().split()))

ans=0
left,right=max(li),sum(li)
while left<=right:
    mid=(left+right)//2

    cnt,sum=0,0
    for i in range(n):
        if sum+li[i]>mid:
            cnt+=1
            sum=0
        sum+=li[i]
    if sum:
        cnt+=1
    if cnt>m:
        left=mid+1
    else:
        right=mid-1
        ans=mid
print(ans)
