#!/usr/bin/env python

while True:
    try:
        s,t=input().split()
        v,f=0,0

        for i in range(len(t)):
            if t[i]==s[v]:
                v+=1
                if v==len(s):
                    f=1
                    break
        if f==1:
            print("Yes")
        else:
            print("No")
    except:
        break

