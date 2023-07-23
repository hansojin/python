#!/usr/bin/env python

n=int(input())

max_li=[]
for i in range(1,n+1):
    my_li=[n]
    my_li.append(i)

    idx=1

    while True:
        next_num=my_li[idx-1]-my_li[idx]
        if next_num<0:
            break
        my_li.append(next_num)
        idx+=1
    if len(max_li)<len(my_li):
        max_li=my_li

print(len(max_li))
print(*max_li)
