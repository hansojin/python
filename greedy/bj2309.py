#!/usr/bin/env python

li=[]
ans=0
for _ in range(9):
    hght=int(input())
    li.append(hght)
    
li.sort()
for i in li:
    for j in li:
            
            if sum(li) - i - j ==100:
                li.remove(i)
                li.remove(j)


for i in li:
    print(i)
