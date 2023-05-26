#!/usr/bin/env python

import sys
input= sys.stdin.readline

li={}
for i in range(int(input())):
    tmp=(input().split('.'))[1]
    if tmp in li:
        li[tmp]+=1
    else:
        li[tmp]=1

li=sorted(li.items())

for k,v in li:
    print(k.rstrip(),v)
