#!/usr/bin/env python

a,b,c,t=map(int,input().split())
flag=0
for A in range(0,t//a+1):
    for B in range(0,t//b+1):
        for C in range(0,t//c+1):
            if a*A+b*B+c*C==t:
                flag=1
                break
print(flag)
