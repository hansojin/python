#!/usr/bin/env python

n=str(input())

ans=0
ln=len(n)
for i in range(ln//2):
    ans+=int(n[i])
for i in range(ln//2,ln):
    ans-=int(n[i])

if ans==0:
    print("LUCKY")
else:
    print("READY")

