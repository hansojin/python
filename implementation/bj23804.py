#!/usr/bin/env python

n=int(input())

for _ in range(n):
    for _ in range(5*n):
        print('@',end='')
    print()
for _ in range(n*3):
    for _ in range(n):
        print('@',end='')
    print()
for _ in range(n):
    for _ in range(5*n):
        print('@',end='')
    print()

