#!/usr/bin/env python

import sys
input= sys.stdin.readline

while True:
    li=list(map(int,input().split()))
    if sum(li)==-1:
        break
    li.sort()
    li.remove(0)
    utl= max(li)//2+1
    cnt=0
    for i in range(len(li)):
        if li[i]>utl:
            break
        if li[i]*2 in li:
            cnt+=1
    print(cnt)

