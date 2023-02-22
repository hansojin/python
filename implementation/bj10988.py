#!/usr/bin/env python

word=str(input())
ln=len(word)
ans=1
for i in range(0,ln//2):
    if word[i]==word[ln-1-i]:
        continue
    else:
        ans=0
        break
print(ans)
