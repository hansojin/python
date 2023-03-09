#!/usr/bin/env python

import sys
input = sys.stdin.readline

a,b=map(int,input().split())
li=list(map(int,input().split()))
lis=[]
for i in range(a-b+1):
    lis.append(sum(li[i:i+b]))


print(max(lis))

