#!/usr/bin/env python

a,b=input().split()
ans=[]

for i in range(len(b)-len(a)+1):
    cnt=0
    for j in range(len(a)):
        if a[j]!=b[j+i]:
            cnt+=1
    ans.append(cnt)
print(min(ans))

