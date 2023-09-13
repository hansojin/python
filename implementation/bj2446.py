#!/usr/bin/env python

n=int(input())
for i in range(n):
    for _ in range(i):
        print(" ",end='')
    for _ in range(2*n-1-2*i):
        print("*",end='')
    print()
if n>1:
    for i in range(2,n+1):
        for _ in range(n-i):
            print(" ",end='')
        for _ in range(2*i-1):
            print("*",end='')
        print()
