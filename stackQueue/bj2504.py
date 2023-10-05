#!/usr/bin/env python

br = list(input())

stack = []
ans = 0
tmp = 1

for i in range(len(br)):

    if br[i] == "(":
        stack.append(br[i])
        tmp *= 2

    elif br[i] == "[":
        stack.append(br[i])
        tmp *= 3

    elif br[i] == ")":
        if not stack or stack[-1] == "[":
            ans = 0
            break
        if br[i-1] == "(":
            ans += tmp
        stack.pop()
        tmp //= 2

    else:
        if not stack or stack[-1] == "(":
            ans = 0
            break
        if br[i-1] == "[":
            ans += tmp

        stack.pop()
        tmp //= 3

if stack:
    print(0)
else:
    print(ans)
