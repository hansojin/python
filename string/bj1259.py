#!/usr/bin/env python

while True:
    num=input()
    if num=='0':
        break
    srt,end=0,len(num)-1
    ans='yes'
    while srt<=end:
        if num[srt]==num[end]:
            srt+=1
            end-=1
        else:
            ans='no'
            break
    print(ans)
