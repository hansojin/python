#!/usr/bin/env python

import sys
input= sys.stdin.readline
from itertools import combinations

x=input().rstrip()
y=input().rstrip()
z=input().rstrip()
k=int(input())

xn = set(combinations(x,k))
yn = set(combinations(y,k))
zn = set(combinations(z,k))

res=list((xn & yn)|(yn&zn)|(zn&xn))

if not res:
    print(-1)
else:
    ans=[]
    for i in res:
        ans.append(''.join(i))

    ans.sort()
    for i in ans:
        print(i)

