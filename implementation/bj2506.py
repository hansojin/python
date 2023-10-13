#!/usr/bin/env python

import sys
input= sys.stdin.readline

n=int(input())
li=list(map(int,input().split()))

for i in range(1,n):
    if li[i-1]!=0 and li[i]!=0:
        li[i]=li[i-1]+1

print(sum(li))
