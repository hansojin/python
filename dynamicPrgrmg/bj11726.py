#!/usr/bin/env python

s=[0,1,2]
for i in range(3,1001):
    s.append(s[i-1]+s[i-2])

print(s[int(input())]%10007)


