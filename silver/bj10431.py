#!/usr/bin/env python

import sys
input= sys.stdin.readline

for _ in range(int(input())):
    li=list(map(int,input().split()))
    cnt=0
    for i in range(1,len(li)-1):
        for j in range(i+1,len(li)):
            if li[i]>li[j]:
                li[i],li[j]=li[j],li[i]
                cnt+=1
    print(li[0],cnt)
