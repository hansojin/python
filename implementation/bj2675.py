#!/usr/bin/env python

n=int(input())

for _ in range(n):
    num,word=input().split()
    
    for i in word:
        print(i*int(num), end='')
    print()
