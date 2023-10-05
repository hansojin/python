#!/usr/bin/env python

n=int(input())
fx=list(input())
num=[int(input()) for i in range(n)]
stack=[]

for i in fx:
    if i.isalpha():
        stack.append(num[ord(i)-65])
    else:
        a=stack.pop()
        res=stack.pop()

        if i=='+':
            res+=a
        elif i=='*':
            res*=a
        elif i=='-':
            res-=a
        elif i=='/':
            res/=a
        stack.append(res)
print('%.2f' %stack[-1])
