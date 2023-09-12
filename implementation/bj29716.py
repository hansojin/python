#!/usr/bin/env python

import sys
input= sys.stdin.readline

cnt=0
j,n = map(int,input().split())
for _ in range(n):
    pl = input().rstrip()
    tmp=0
    for i in pl:
        if i.islower():
            tmp+=2
        elif i.isupper():
            tmp+=4
        elif i==' ':
            tmp+=1
        else:
            tmp+=2
    if tmp<=j:
        cnt+=1
print(cnt)
