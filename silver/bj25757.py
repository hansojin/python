#!/usr/bin/env python

import sys
input= sys.stdin.readline

n,m=map(str,input().split())
li=[]
for _ in range(int(n)):
    li.append(input().rstrip())
li=set(li)
if m=='Y':
    print(len(li))
elif m=='F':
    print(len(li)//2)
else:
    print(len(li)//3)
