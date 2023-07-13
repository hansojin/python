#!/usr/bin/env python

A=str(input())
B=str(input())

for i in A:
    if i in B:
        B=B.replace(i,'',1)
        A=A.replace(i,'',1)
print(len(A)+len(B))
