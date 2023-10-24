#!/usr/bin/env python

import sys
input= sys.stdin.readline

n,m=map(int,input().split())
li=sorted(list(map(int,input().split())))

for _ in range(m):
    tmp = li[0]+li[1]
    li[0],li[1]=tmp,tmp
    li.sort()

print(sum(li))
