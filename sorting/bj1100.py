#!/usr/bin/env python

li=[]
for _ in range(8):
    tmp=str(input())
    li.append(list(map(str,str(tmp))))
cnt=0
for i in range(8):
    if i%2==0:
        for j in range(0,8,2):
            if li[i][j]=='F':
                cnt+=1
    else:
        for j in range(1,8,2):
            if li[i][j]=='F':
                cnt+=1
print(cnt)
