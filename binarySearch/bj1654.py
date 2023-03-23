#!/usr/bin/env python

import sys
input = sys.stdin.readline

k,n=map(int,input().split())
lan=[int(input()) for _ in range(k)]

minn=1
maxx=max(lan)

while minn<=maxx:
    mid=(minn+maxx)//2
    cnt=0
    for i in lan:
        cnt+=i//mid

    if cnt>=n:
        minn=mid+1
    else:
        maxx=mid-1

print(maxx)
