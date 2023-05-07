#!/usr/bin/env python
dp=[0 for _ in range(491)]
dp[1]=1
for i in range(2,491):
    dp[i]=dp[i-1]+dp[i-2]

while True:
    hour= int(input())
    if hour == -1:
        break
    else:
        print(f'Hour {hour}: {dp[hour]} cow(s) affected')

