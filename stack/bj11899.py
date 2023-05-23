#!/usr/bin/env python

stack=[]
gh=input()

for i in gh:
    if i=='(':
        stack.append(i)
    elif i==')':
        if stack and stack[-1]=='(':
            stack.pop()
        else:
            stack.append(i)
print(len(stack))
