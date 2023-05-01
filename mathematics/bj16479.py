#!/usr/bin/env python

k=int(input())
d1,d2=map(int,input().split())

if d1==d2:
    print(k**2)
elif d1==3*d2:
    print(k**2-d2**2)
else:
    print(k**2 - ((d1-d2)/2)**2)
