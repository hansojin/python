#!/usr/bin/env python

import sys
input=sys.stdin.readline

def mkTuple(list):
    return tuple(list)

n=int(input())
li=[]
for _ in range(n):
    num=list(map(int,input().split()))
    li.append(mkTuple(num))

li=sorted(li)

for i in range(n):
    print(li[i][0],li[i][1])

