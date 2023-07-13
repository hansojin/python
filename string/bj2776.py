#!/usr/bin/env python

import sys
input= sys.stdin.readline

for _ in range(int(input())):
    n=int(input())
    nLi=set(map(int,input().split()))
    m=int(input())
    mLi=list(map(int,input().split()))
    
    for i in mLi:
        print(1 if i in nLi else 0)
