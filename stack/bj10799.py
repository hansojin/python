#!/usr/bin/env python

pipe=list(input())
stack=[]
cnt=0
for i in range(len(pipe)):
    if pipe[i]=='(':
        stack.append('(')
        
    else:
        if pipe[i-1]=='(':
            stack.pop()
            cnt+=len(stack)
        else:
            stack.pop()
            cnt+=1
print(cnt)
