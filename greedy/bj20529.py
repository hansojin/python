#!/usr/bin/env python

import sys
input= sys.stdin.readline
from itertools import combinations

def mbti(a,b):
    dist=0
    for i,j in zip(a,b):
        if i!=j:
            dist+=1
    return dist

for _ in range(int(input())):
    n=int(input())
    mb=input().rstrip().split()
    if n>32:
        print(0)
    else:
        res=13
        case=combinations(mb,3)
        for a,b,c in case:
            dist=0
            dist+=mbti(a,b)
            dist+=mbti(a,c)
            dist+=mbti(b,c)

            res=min(res,dist)
        print(res)
