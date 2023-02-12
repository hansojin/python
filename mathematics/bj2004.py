#!/usr/bin/env python

from math import factorial as fac
a,b=map(int,input().split())

f=fac(a)//(fac(b)*fac(a-b))
f=str(f)[::-1]
cnt=0
if f[0]=='0':
    while f[cnt]=='0':
        cnt+=1
print(cnt)
