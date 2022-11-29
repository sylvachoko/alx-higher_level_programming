#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        numbers = number * -1
        minus = numbers % 10
        last_digit = minus * -1
    else:
        last_digit = number % 10
    print(f"{last_digit}")
