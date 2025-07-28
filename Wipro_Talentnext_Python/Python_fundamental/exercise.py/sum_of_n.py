#Write a program to print the sum of all the digits of a given number.
def sum_upto_n(n):
    return n * (n + 1) // 2
num = int(input())
print(sum_upto_n(num))