#!/usr/bin/env python

import sys
input= sys.stdin.readline
n = int(input())
print(int(n*(n-1)*(n-2)*(n-3)/24))
