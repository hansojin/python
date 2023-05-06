#!/usr/bin/env python

doc=input()
word=input()
cnt=0

doc=doc.replace(word,'*')
for i in doc:
    if i=='*':
        cnt+=1
print(cnt)
