#!/usr/bin/env python

word=input().rstrip()
wlen=len(word)
flag=True
for i in range(wlen//2):
    if word[i]!=word[wlen-i-1]:
        flag=False
        break
if flag:
    print('true')
else:
    print("false")
