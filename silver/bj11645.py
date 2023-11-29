#!/usr/bin/env python

import sys
input= sys.stdin.readline

for _ in range(int(input())):
    s=set()
    for _ in range(int(input())):
        s.add(input())
    print(len(s))
