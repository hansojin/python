#!/usr/bin/env python

import sys
input= sys.stdin.readline

x,y,z=map(int,input().split())
li=[]
for i in range(int(input())):
    a,b,c=0,0,0
    for _ in range(3):
        ta,tb,tc=map(int,input().split())
        a+=ta
        b+=tb
        c+=tc
    li.append(a*x+b*y+c*z)
print(max(li))
