#Write a function to calculate and return the factorial of a number (a non-negative integer).
def factorial(n):
    if n == 0:
        return 1  
    elif n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

N = int(input())
print(factorial(N))