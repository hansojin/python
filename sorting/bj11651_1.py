#!/usr/bin/env python
import sys
input = sys.stdin.readline


n=int(input())

li=[]
for i in range(n):
    a,b=map(int,input().split())
    li.append([b,a])

li=sorted(li)

for y,x in li:
    print(x,y)

