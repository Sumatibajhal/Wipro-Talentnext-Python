#Given two non-negative values, print true if they have the same last digit, such as with 27 and 57

def same_last_digit(a, b):
    return (a % 10) == (b % 10)

num1 = int(input())
num2 = int(input())

print(same_last_digit(num1, num2))