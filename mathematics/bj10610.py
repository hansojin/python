#!/usr/bin/env python

n=int(input())
li=list(map(int,str(n)))
li.sort(reverse=True)

if n%3!=0:
    print(-1)

elif li[-1]!=0:
    print(-1)

else:
    for i in range(len(li)):
        
        print(li[i],end='')
