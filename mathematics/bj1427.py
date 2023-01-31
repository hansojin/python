#!/usr/bin/env python

n=list(str(input()))
n.sort(reverse=True)
m=''.join(n)
print(m)

# print(*sorted(input())[::-1],sep='')

