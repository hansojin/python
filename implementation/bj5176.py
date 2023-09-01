#!/usr/bin/env python

import sys
input= sys.stdin.readline

for _ in range(int(input())):
    n,m=map(int,input().split())
    li=[0 for _ in range(m+1)]
    for i in range(n):
        ch=int(input())
        li[ch]=1
    print(n-sum(li))
