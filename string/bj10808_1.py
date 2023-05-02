#!/usr/bin/env python

word=str(input())
li=[0]*26
for i in word:
    li[ord(i)-ord('a')]+=1

for i in li:
    print(i,end=' ')
