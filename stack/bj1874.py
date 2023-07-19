#!/usr/bin/env python

n = int(input())
stack=[]
ans=[]
flag = True
cnt=1
for i in range(n):
    num = int(input())
    while cnt <= num:       
        stack.append(cnt)
        ans.append("+")
        cnt += 1

    if stack[-1] == num:    
        stack.pop()         
        ans.append("-")
    else:                           
        flag = False            
        break               

if flag:
    for i in ans:
        print(i)
else:
    print("NO")
