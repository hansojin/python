#!/usr/bin/env python

a,b=[],[]
for _ in range(3):
    a.append(int(input()))
for _ in range(3):
    b.append(int(input()))
sa,sb=0,0
for i in range(3):
    sa+=a[i]*(3-i)
    sb+=b[i]*(3-i)
if sa>sb:
    print("A")
elif sa<sb:
    print("B")
else:
    print("T")
