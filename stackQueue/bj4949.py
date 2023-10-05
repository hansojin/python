#!/usr/bin/env python

while True:
    stack=[]
    sen=list(map(str,input()))
    if sen[0]==".":
        break
    else:
        for j in sen:
            for i in j:
                if i=='[':
                    stack.append('[')
                if i==']':
                    if len(stack)==0:
                        stack.append(']')
                        break
                    if stack[-1]=='[':
                        stack.pop()
                    else:
                        stack.append(']')
                        break
                if i=='(':
                    stack.append('(')
                if i==')':
                    if len(stack)==0:
                        stack.append(')')
                        break
                    if stack[-1]=='(':
                        stack.pop()
                    else:
                        stack.append(')')
                        break
    if len(stack)==0:
        print("yes")
    else:
        print("no")


