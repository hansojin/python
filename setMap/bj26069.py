#!/usr/bin/env python

import sys
input= sys.stdin.readline

li=set()
for _ in range(int(input())):
    a,b=map(str,input().split())
    if a=='ChongChong' or b=='ChongChong':
        li.add(a)
        li.add(b)
    elif a in li:
        li.add(b)
    elif b in li:
        li.add(a)
print(len(li))
