#!/usr/bin/env python

import sys
input= sys.stdin.readline

n=int(input())
li=[int(input()) for _ in range(n)]
li.sort()
for i in li:
    print(i)
