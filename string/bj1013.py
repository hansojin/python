#!/usr/bin/env python

import sys
input= sys.stdin.readline
import re

res=[]
n=int(input())
for _ in range(n):
    sign = input().replace('\n','')
    p=re.compile('(100+1+|01)+')
    m=p.fullmatch(sign)
    if m:
        res.append("YES")
    else:
        res.append("NO")

for i in res:
    print(i)
