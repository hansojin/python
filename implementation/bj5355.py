#!/usr/bin/env python

for _ in range(int(input())):
    li = list(map(str, input().split()))
    ans = 0
    for i in range(len(li)):
        if i == 0:
            ans += float(li[i])
        else:
            if li[i] == "#":
                ans -= 7
            elif li[i] == "%":
                ans += 5
            elif li[i] == "@":
                ans *= 3

    print("%0.2f" % ans)
