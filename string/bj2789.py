#!/usr/bin/env python

s=input()
no=['C','A','M','B','R','I','D','E','G','E']

for i in s:
    if i in no:
        s=s.replace(i,'')
print(s)
