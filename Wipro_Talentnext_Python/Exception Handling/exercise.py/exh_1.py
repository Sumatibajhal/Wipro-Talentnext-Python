#Write a program to accept two numbers from the user and perform division. If any exception occurs, print an error message or else print the result.
try:
    num1 = float(input("Enter 1st num: "))
    num2 = float(input("Enter 2nd number: "))
    result = num1 / num2
    print(f"The result of division is: {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Please enter valid numeric values.")
