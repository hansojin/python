#!/usr/bin/env python

import sys
input= sys.stdin.readline
from math import gcd, sqrt

n=int(input())
li=[]

if n==2:
    a,b=map(int,input().split())
    gcdd = gcd(a,b)
    
else:
    a,b,c=map(int,input().split())
    gcdd = gcd(gcd(a,b),c)

for i in range(1,int(sqrt(gcdd))+1):
    if gcdd%i==0:
        li.append(i)
        if i**2!=gcdd:
            li.append(gcdd//i)
li.sort()
for n in li:
    print(n)
