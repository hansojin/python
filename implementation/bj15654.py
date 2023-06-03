#!/usr/bin/env python

import sys
input= sys.stdin.readline

from itertools import permutations

n,m=map(int,input().split())
li=list(map(int,input().split()))
li.sort()

tmp=permutations(li,m)
for i in tmp:
    for j in range(len(i)):
        print(i[j],end=' ')
    print()
