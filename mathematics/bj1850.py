#!/usr/bin/env python

def gcd(x,y):
    mod = x%y
    while mod>0:
        x=y
        y=mod
        mod=x%y
    return y

n,m=map(int,input().split())
print('1'*gcd(n,m))
