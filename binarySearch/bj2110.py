#!/usr/bin/env python

import sys
input= sys.stdin.readline

n,m=map(int,input().split())
li=[int(input()) for _ in range(n)]
li.sort()

def binary(arr,s,e):
    while s<=e:
        mid =(s+e)//2
        cur = arr[0]
        cnt=1

        for i in range(1, len(arr)):
            if arr[i]>=cur+mid:
                cnt+=1
                cur=arr[i]

        if cnt>=m:
            global ans
            s=mid+1
            ans=mid
        else:
            e=mid-1
s=1
e=li[-1]
ans=0

binary(li,s,e)
print(ans)
