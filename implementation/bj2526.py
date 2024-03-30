#!/usr/bin/env python

a,b=map(int, input().split())
l=[]
n=a
while True:
    n=n*a%b
    if n in l:
        print(len(l)-l.index(n))
        break
    l.append(n)
