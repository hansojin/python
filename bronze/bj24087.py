#!/usr/bin/env python

s = int(input())
a = int(input())
b = int(input())

r = 250
if s <= a:
    print(r)
else:
    r += ((s-a)//b)*100
    if (s-a) % b != 0:
        r += 100
    print(r)
