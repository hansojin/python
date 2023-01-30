#!/usr/bin/env python

m=int(input())
n=int(input())
ans_list=[]
for i in range(m,n+1):

    cnt=0
    for a in range(1,i+1):
        if i%a==0:
            cnt+=1
    if cnt==2:
        ans_list.append(i)

if sum(ans_list)==0:
    print(-1)
else:
    print(sum(ans_list))
    print(min(ans_list))

