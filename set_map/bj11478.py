#!/usr/bin/env python

word = input()
ln=len(word)
sset=set()

for i in range(ln):
    for j in range(ln):
        sset.add(word[i:j+1])
print(len(sset)-1)



