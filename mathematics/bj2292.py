#!/usr/bin/env python

n=int(input())

sum=1
for i in range(100000000):
    sum+=6*i
    if sum>=n:
        print(i+1)
        break
