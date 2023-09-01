#!/bin/env python

n=int(input())
for i in range(1,10102):
    if i*(i+1)==n-1:
        print(i)
        break
