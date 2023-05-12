#!/usr/bin/env python

import sys
input= sys.stdin.readline

n=int(input())
order=list(map(int,input().split()))
li=[0 for _ in range(n)]
for i in range(n):
    li.insert(int(i-order[i]),i+1)
for i in range(n):
    print(li[i],end=' ')
