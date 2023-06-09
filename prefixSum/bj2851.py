#!/usr/bin/env python

import sys
input= sys.stdin.readline

prefix=[0]*(11)
for i in range(10):
    tmp=int(input())
    prefix[i+1]=prefix[i]+tmp

hund=1e9
for i in range(1,11):
    if abs(prefix[i]-100)<=hund:
        hund=abs(prefix[i]-100)
        ans=prefix[i]
print(ans)

