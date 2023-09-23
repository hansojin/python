#!/usr/bin/env python

p,m=0,0
for _ in range(10):
    o,i=map(int,input().split())
    p+=i-o
    m=max(p,m)
print(m)
