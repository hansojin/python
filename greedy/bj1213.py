#!/usr/bin/env python

from collections import Counter

word=list(map(str,input()))
word.sort()
check= Counter(word)

cnt = 0
ans = ''
mid= ''

for i in check:
    if check[i]%2!=0:
        cnt+=1
        mid+=i
    for _ in range(check[i]//2):
        ans+=i

if cnt>1:
    print("I'm Sorry Hansoo")
elif cnt==0:
    print(ans+ans[::-1])
else:
    print(ans+mid+ans[::-1])
