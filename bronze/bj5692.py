#!/usr/bin/env python

import sys
input= sys.stdin.readline
import math

while True:
    n=input().rstrip()
    if n=='0':
        break
    l=len(n)
    ans=0
    for i in n:
        ans+=int(i)*math.factorial(l)
        l-=1
    print(ans)

