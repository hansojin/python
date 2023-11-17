#!/usr/bin/env python

k=int(input())
a,b,c,d=map(int,input().split())

tmp = a*k+b
if tmp == c*k+d:
    print("Yes", tmp)
else:
    print("No")

