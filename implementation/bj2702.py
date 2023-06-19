#!/usr/bin/env python

import sys
input= sys.stdin.readline

def gcd(a,b):
    if a==0:
        return b
    else:
        return gcd(b%a,a)


def lcm(a,b):
    return int((a*b)/gcd(a,b))

for _ in range(int(input())):
    a,b=map(int,input().split())
    print(lcm(a,b),gcd(a,b))
