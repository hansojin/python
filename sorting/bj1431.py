#!/usr/bin/env python

import sys
input = sys.stdin.readline

def numsum(x):
    res=0
    for i in x:
        if i.isdigit():
            res+=int(i)
    return res

n=int(input())
li=[]
for _ in range(n):
    tmp=input().strip()
    li.append(tmp)
li.sort(key=lambda x :(len(x),numsum(x),x))

for i in li:
    print(i)
