#!/usr/bin/env python

n=input().rstrip()
for i in n:
    if i.isdigit():
        n=n.replace(i,'')
m=input().rstrip()
if m in n:
    print(1)
else:
    print(0)
