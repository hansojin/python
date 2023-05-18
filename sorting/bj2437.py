#!/usr/bin/env python

import sys
input= sys.stdin.readline

n=int(input())
li=list(map(int,input().split()))
li.sort()

tmp=1

for i in li:
    if tmp<i:
        break
    else: tmp+=i
print(tmp)
