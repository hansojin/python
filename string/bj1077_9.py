#!/usr/bin/env python

def can_form_valid_parentheses(s):
    balance = 0
    wildcard_open = 0

    for char in s:
        if char == '(':
            balance += 1
        elif char == ')':
            if balance > 0:
                balance -= 1
            elif wildcard_open > 0:
                wildcard_open -= 1
            else:
                return "NO"
        elif char == '*':
            wildcard_open += 1

    if balance <= wildcard_open:
        return "YES"
    else:
        return "NO"

T = int(input())
for _ in range(T):
    S = input()
    result = can_form_valid_parentheses(S)
    print(result)

