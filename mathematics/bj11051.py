#!/usr/bin/env python

from math import factorial as fac
a,b=map(int,input().split())

res=fac(a)//(fac(b)*fac(a-b))
print(int(res%10007))
