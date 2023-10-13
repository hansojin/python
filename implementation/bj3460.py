#!/usr/bin/env python

import sys
input= sys.stdin.readline

for _ in range(int(input())):
    li=[]
    n=int(input())
    while(n!=0):
        li.append(n%2)
        n//=2
    for i in range(len(li)):
        if li[i]==1:
            print(i,end=' ')
