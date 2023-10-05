#!/usr/bin/env python

n = int(input())
word = input()
cnt = 0
ls, cs =0,0

for i in word:
    if i=='L':
        ls+=1
    elif i=='R':
        if ls>=0:
            cnt+=1
            ls-=1
        else:
            break
    elif i=='S':
        cs+=1
    elif i=='K':
        if cs>0:
            cnt+=1
            cs-=1
        else:
            break
    else:
        cnt+=1
print(cnt)
