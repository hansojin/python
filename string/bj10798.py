#!/usr/bin/env python

li=[]
for _ in range(5):
    li.append(str(input()))

for i in range(15):
    for j in range(5):
        if i<len(li[j]):
            print(li[j][i],end='')
    
