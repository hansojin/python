#!/usr/bin/env python

n=int(input())
b=input().rstrip()

for i in b[::n]:
    print(i,end='')
