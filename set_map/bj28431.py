#!/usr/bin/env python

li=[]
for _ in range(5):
    i=int(int(input()))
    if i in li:
        li.remove(i)
    else:
        li.append(i)
print(li[0])
