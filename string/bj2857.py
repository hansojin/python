#!/usr/bin/env python

arr=[]
for i in range(5):
    name=input()
    if len(name)>10:
        continue
    name=name.replace("FBI","*");
    if name.find("*")==-1:
        continue
    arr.append(i+1)
if arr:
    print(*arr)
else:
    print("HE GOT AWAY!")

