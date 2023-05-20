#!/usr/bin/env python

p=str(input())
for i in p:
    if i.islower():
        print(i.upper(),end='')
    else:
        print(i,end='')
