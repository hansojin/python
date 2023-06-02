#!/usr/bin/env python

n,b=input().split()
j,ans=0,0
b=int(b)
for i in n[::-1]:
    if i.isdigit():
        ans+=int(i)*(b**j)
        j+=1
    else:
        ans+=(ord(i)-55)*(b**j)
        j+=1
print(ans)
