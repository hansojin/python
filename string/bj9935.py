#!/usr/bin/env python

s=input()
target=input()

while True:
    if target in s:
        s=s.replace(target,'')
    else:
        break

if len(s)!=0:
    print(s)
else:
    print("FRULA")
