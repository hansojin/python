#!/usr/bin/env python

import sys
input= sys.stdin.readline

for _ in range(int(input())):
    n=input().rstrip()
    s=set()
    for i in n:
        s.add(i)
    s=list(s)
    print(len(s))
