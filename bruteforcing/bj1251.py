#!/usr/bin/env python

word = list(input())
ans,tmp = [],[]
l=len(word)

for i in range(1, l- 1):
    for j in range(i + 1,l):
        a = word[:i]
        b = word[i:j]
        c = word[j:]
        a.reverse()
        b.reverse()
        c.reverse()
        tmp.append(a + b + c)

for a in tmp:
    ans.append(''.join(a))

print(sorted(ans)[0])
