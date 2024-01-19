#!/usr/bin/env python

import sys
input= sys.stdin.readline

c,k,p=map(int,input().split())
tmp=0
for i in range(1,c+1):
    tmp+=i*(k+p*i)
print(tmp)

