#!/usr/bin/env python

import sys
input =sys.stdin.readline

n=int(input())
li=list(map(int,input().split()))

def yy(n):
    return (n//30)*10+ 10 

def mm(n):
    return (n//60)*15 + 15 

y,m=0,0
for i in li:
    y+=yy(i)
    m+=mm(i)
if y>m:
    print("M", m)
elif y<m:
    print("Y", y)
else:
    print("Y M", y)

