#!/usr/bin/env python

a,b=map(int,input().split())

def gcd(a,b):
    while(b):   # a%b!=0 
        a,b=b,a%b
    return a

ans=gcd(a,b)
print(ans)
print(a*b//ans)
