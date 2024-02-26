#!/usr/bin/env python

order=input().rstrip()
li=[0,1,0,0,2]

def change(a,b):
    li[a],li[b]=li[b],li[a]

for i in order:
    if i=='A':
        change(1,2)
    elif i=='B':
        change(1,3)
    elif i=='C':
        change(1,4)
    elif i=='D':
        change(2,3)
    elif i=='E':
        change(2,4)
    elif i=='F':
        change(3,4)
print(li.index(1))
print(li.index(2))
