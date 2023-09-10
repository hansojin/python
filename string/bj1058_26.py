#!/usr/bin/env python

li = ['Never gonna give you up',
'Never gonna let you down',
'Never gonna run around and desert you',
'Never gonna make you cry',
'Never gonna say goodbye',
'Never gonna tell a lie and hurt you',
'Never gonna stop']

flag = True
n=int(input())
for i in range(n):
    word = input()
    if word in li:
        continue
    else:
        flag = False
        break
if flag:
    print("No")
else:
    print("Yes")
