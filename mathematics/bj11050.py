#!/usr/bin/env python

def fac(n):
    if n>1: 
        return n*fac(n-1)
    else:
        return 1

a,b=map(int,input().split())
print(fac(a)//(fac(b)*fac(a-b)))
