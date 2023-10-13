#!/usr/bin/env python

n=int(input())
for i in range(n):
    for j in range(n-1-i):
        print(" ",end='')
    if i==0 or i==n-1:
        for j in range(2*i+1):
            print("*",end='')
    else:
        print("*",end='')
        for j in range(2*i-1):
            print(" ",end='')
        print("*",end='')
    print()

