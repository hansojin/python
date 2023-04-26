#!/usr/bin/env python

a,b,c=map(int,input().split())

n=a*b
ans=n//c
ans=list(map(str,ans))
for i in range(20):
    n%c;
    n*10
    ans.append('.')
    if n<c:
        ans.append('0')
    else:
        ans.append('0'+n/c)
print(ans)

