#!/usr/bin/env python

import sys
input= sys.stdin.readline

s=set()
for _ in range(int(input())):
    n="".join(sorted(input().rstrip()))
    s.add(n)
print(len(s))

