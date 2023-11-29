#!/usr/bin/env python

import sys
input= sys.stdin.readline
from collections import Counter

n=int(input())
li=input().split()
for _ in range(n):
    li+=input().split()
li=list(li)
for i in Counter(li).most_common():
    print(i[0],i[1]-1)

