#!/usr/bin/env python

n=input()
f=int(input())
num=int(n[:-2]+'00')
while True:
    if num%f==0:
        break
    num+=1
print(str(num)[-2:])
