#!/usr/bin/env python

s=input()
if '7' in s:
    if int(s)%7==0:
        print(3)
    else:
        print(2)
else:
    if int(s)%7==0:
        print(1)
    else:
        print(0)
