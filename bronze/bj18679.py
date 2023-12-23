#!/usr/bin/env python

import sys
input= sys.stdin.readline
A,B=[],[]
for _ in range(int(input())):
    a,b=map(str,input().rstrip().split(' = '))
    A.append(a)
    B.append(b)

for _ in range(int(input())):
    n=int(input())
    sen=input().split()
    for i in range(n):
        print(B[A.index(sen[i])],end=' ')
    print()
