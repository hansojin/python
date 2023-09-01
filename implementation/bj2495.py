#!/usr/bin/env python

for _ in range(3):
    num=input()
    cnt=1
    ans=[1]
    for i in range(len(num)-1):
        if num[i]==num[i+1]:
            cnt+=1
            ans.append(cnt)
        else:
            cnt=1
    print(max(ans))

