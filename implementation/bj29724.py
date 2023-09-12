#!/usr/bin/env python

import sys
input= sys.stdin.readline
W,A = 0,0
for _ in range(int(input())):
    op,a,b,c=input().split()
    tmp=1
    if op=='A':
        tmp*=int(a)//12
        tmp*=int(b)//12
        tmp*=int(c)//12
        W += (1000 + 500*tmp)
        A += 4000* tmp
    if op=='B':
        W += 6000
print(W)
print(A)
