#!/usr/bin/env python

from itertools import combinations

def gcd(x,y):
    while y:
        x,y=y,x%y
    return x

n=int(input())
li=[]

for _ in range(n):
    li=list(map(int,input().split()))
    li=li[::-1]
    del li[-1]
    com=combinations(li,2)
    res=0
    for i in com:
        res+=gcd(i[0],i[1])
    print(res)
    
