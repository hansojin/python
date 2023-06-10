#!/usr/bin/env python

word=input()
cnt=0
mobis=['M','O','B','I','S']

for i in mobis:
    if word.find(i)!=-1:
        cnt+=1
if cnt==5:
    print("YES")
else:
    print("NO")
