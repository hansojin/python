#!/usr/bin/env python

import sys
input = sys.stdin.readline

n=input()
li=list(map(int,input().split()))
lis=set(li)
lis=list(lis)
lis.sort()
for i in li:
    print(lis.index(i),end=' ')
