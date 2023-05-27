#!/usr/bin/env python

n=input()
nl=len(n)-1
c,i=0,0
while i<nl:
    c+=9*(10**i)*(i+1)
    i+=1
c+=((int(n)-(10**nl))+1)*(nl+1)
print(c)
