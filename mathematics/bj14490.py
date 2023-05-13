#!/usr/bin/env python

def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

a,b=map(int,input().split(":"))
x=gcd(a,b)

print(f'{a//x}:{b//x}')
