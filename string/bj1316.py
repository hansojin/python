#!/usr/bin/env python

n=int(input())
cnt=n
for _ in range(n):
    word=input()
    for idx in range(len(word)-1):
        if word[idx]!= word[idx+1]:
            if word[idx+1] in word[:idx]:
                cnt-=1
                break
print(cnt)
