import sys

readline = sys.stdin.readline

pair_dic = {"(": ")", "[": "]"}

while True:
    string = readline().rstrip()
    if string == ".":
        break

    stack = []
    brackets = list(string)
    for b in brackets:
        if b == "(" or b == "[":
            stack.append(b)
        elif b == ")" or b == "]":
            if len(stack) == 0:
                stack.append(b)
                break
            if pair_dic[stack[-1]] != b:
                break
            stack.pop()

    print("yes" if len(stack) == 0 else "no")
