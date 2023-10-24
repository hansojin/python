#!/usr/bin/env python

li=[0,4,6]
for i in range(3,81):
    li.append(li[i-1]+li[i-2])

print(li[int(input())])
