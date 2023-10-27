#!/usr/bin/env python

s=input()
t=input()

sl,tl = len(s),len(t)

if s*tl == t*sl:
    print(1)
else:
    print(0)
