#!/usr/bin/env python

def get_next_value(current_values):
    if current_values[0] == "FizzBuzz":
        return "Fizz" if current_values[2] % 3 == 0 else str(current_values[2])
    elif current_values[0] == "Fizz":
        return "Buzz" if current_values[2] % 5 == 0 else str(current_values[2])
    elif current_values[0] == "Buzz":
        return "Fizz" if current_values[2] % 3 == 0 else str(current_values[2])
    else:
        return "FizzBuzz" if current_values[2] % 3 == 0 and current_values[2] % 5 == 0 else str(current_values[2])

input_strings = []
for _ in range(3):
    input_strings.append(input())

current_values = [input_strings[0], input_strings[1], int(input_strings[2])]

next_value = get_next_value(current_values)
print(next_value)

