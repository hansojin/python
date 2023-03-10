#!/usr/bin/env python

import sys
input = sys.stdin.readline

n,m=map(int,input().split())
li=list(map(int,input().split()))
a=[0]
tmp=0
for i in li:
    tmp+=i
    a.append(tmp)





