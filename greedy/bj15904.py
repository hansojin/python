#!/usr/bin/env python

sen=input()
word=['U','C','P','C']
check=True

for i in range(len(word)):
    if word[i] in sen:
        idx=sen.find(word[i])
        sen=sen[idx+1:]
    else:
        check=False
        break
if check==True:
    print("I love UCPC")
else:
    print("I hate UCPC")
