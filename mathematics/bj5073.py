#!/usr/bin/env python

import sys
input = sys.stdin.readline

while True:
    a,b,c=map(int,input().split())
    if a==0 and b==0 and c==0:
        break
    if max(a,b,c)>=(a+b+c)-max(a,b,c):
        print('Invalid')

    else:
        if a==b==c:
            print('Equilateral')
        elif a!=b and b!=c and c!=a:
            print('Scalene')
        else:
            print('Isosceles')

