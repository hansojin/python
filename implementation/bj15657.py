#!/usr/bin/env python

import sys
input= sys.stdin.readline

from itertools import combinations_with_replacement

n,m=map(int,input().split())
li=list(map(int,input().split()))
li=sorted(li)

for i in list(combinations_with_replacement(li,m)):
    for j in i:
        print(j,end=' ')
    print()

