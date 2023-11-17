#!/usr/bin/env python

r,c,n=map(int,input().split())
if r%n==0:
    a=r//n
else:
    a=r//n+1
if c%n==0:
    a*=c//n
else:
    a*=c//n+1
print(a)
