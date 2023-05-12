#!/usr/bin/env python

a,b=map(int,input().split())
al=list(map(int,input().split()))
bl=list(map(int,input().split()))
al,bl=set(al),set(bl)
cl=al-bl
cl=list(cl)
cl.sort()
print(len(cl))
print(*cl)
