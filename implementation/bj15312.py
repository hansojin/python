#!/usr/bin/env python

boy = input()
girl = input()
ln=len(boy)
alpha=[3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

li=[]
for i in range(ln):
    li.append(alpha[ord(boy[i])-65])
    li.append(alpha[ord(girl[i])-65])
lli=len(li)
while lli>2:
    tmp=[]
    for i in range(lli-1):
        tmp.append(li[i]+li[i+1])
    li=tmp
    lli=len(li)
print(str(li[0])[-1],end='')
print(str(li[1])[-1])

