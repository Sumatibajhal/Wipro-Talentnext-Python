#Write a program to accept 10 numbers through command line arguments and calculate the sum of prime numbers among them.

import sys

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

if len(sys.argv) != 11:
    print("Usage: python script.py 1 2 2 3 4 5 6 7 8 9 10")
else:
    try:
        numbers = [int(arg) for arg in sys.argv[1:]]
        prime_num = [num for num in numbers if is_prime(num)]
        prime_sum = sum(prime_num)
        print(f"Prime numbers found: {prime_num}")
        print(f"Sum of prime numbers: {prime_sum}")
    except ValueError:
        print("Please enter valid integer numbers.")
