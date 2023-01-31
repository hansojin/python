#!/usr/bin/env python

a,b=map(int,input().split())
num=list(map(int,input().split()))

num.sort(reverse=True)
print(num[b-1])

# num.sort()
# print(num[-b])
