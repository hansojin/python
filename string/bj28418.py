#!/usr/bin/env python

a,b,c= map(int,input().split())
d,e = map(int,input().split())

A = a*d*(d-1)
B = 2*a*d*e
C = a*e*e + b*e + c*(1-d) - e

D = B*B - 4*A*C

if A!=0:
    if D>0:
        print("Go ahead")
    elif D==0:
        print("Remember my character")
    else:
        print("Head on")
else: 
    if B==C==0:
        print("Nice")
    elif B!=0 and C!=0:
        print("Remember my character")
    else:
        print("Head on")
