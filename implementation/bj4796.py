#!/usr/bin/env python

import sys
input= sys.stdin.readline

n=1
while True:
    a,b,c=map(int,input().split())
    if a==b==c==0:
        break
    num=(c//b)*a+min((c%b),a)
    print(f'Case {n}: {num}')
    n+=1
