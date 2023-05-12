#!/usr/bin/env python

n=int(input())
cnt=0
for i in range(n):
    stack=[]
    word=str(input())
    for i in word:
        if not stack:
            stack.append(i)
        elif stack:
            if stack[-1]==i:
                stack.pop()
            else:
                stack.append(i)
    if not stack:
        cnt+=1
print(cnt)
