#!/usr/bin/env python

li=[]
for _ in range(int(input())):
    word=str(input())
    li.append(word)

for word in li:

    tmp=[]
    for i in word[::-1]:
        tmp.append(i)
        word=(''.join(map(str,tmp)))
        
        if word in li:
            ans=word
            length=len(ans)
            break

print(length,ans[length//2])

