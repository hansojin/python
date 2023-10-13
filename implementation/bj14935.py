#!/usr/bin/env python

n=int(input())
diff=n
cnt=1e5
flag = False
while (cnt>0):
    cnt-=1
    strn = str(n)
    n=int(len(strn))*int(strn[0])
    if(n==diff):
        print("FA")
        flag=True
        break
    else:
        diff=n
if flag==False:
    print("NFA")
