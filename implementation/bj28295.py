#!/usr/bin/env python

way=0
for _ in range(10):
    n=int(input())
    if n==1:
        way+=1
    elif n==2:
        way+=2
    elif n==3:
        way-=1
if way<0:
    way+=12

w=way%4
if w==0:
    print('N')
elif w==1:
    print('E')
elif w==2:
    print('S')
else:
    print('W')
