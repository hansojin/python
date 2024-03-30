#!/usr/bin/env python

n=int(input())

for _ in range(2):
    for _ in range(n):
        print("@"*n,end='')
        print(" "*3*n,end="")
        print("@"*n,end="")
        print()
    for _ in range(n):
        print("@"*5*n)
for _ in range(n):
    print("@"*n,end='')
    print(" "*3*n,end="")
    print("@"*n,end="")
    print()



