#!/usr/bin/env python

s=input()
target=input()

stack=[]
tlen=len(target)

for i in range(len(s)):
    stack.append(s[i])
    if ''.join(stack[-tlen:])==target:
        for _ in range(tlen):
            stack.pop()
print(stack)
if stack:
    print(''.join(stack))
else:
    print("FRULA")
