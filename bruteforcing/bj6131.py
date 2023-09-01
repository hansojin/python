#!/usr/bin/env python

n=int(input())
end= (n+1)//2+1
ans=0
for b in range(1,end):
    for a in range(b+1,end):
        if (a+b)*(a-b)==n:
            ans+=1
print(ans)
