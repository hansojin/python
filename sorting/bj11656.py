#!/usr/bin/env python

word=input()
li=[]
for i in range(len(word)):
    li.append(word[i:])

li.sort()
for i in li:
    print(i)
