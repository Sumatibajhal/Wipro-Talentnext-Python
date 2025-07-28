#Declare a list with 10 integers and ask the user to enter an index. Check whether the number in that index is positive or negative number. If any invalid index is entered, handle the exception and print an error message.
numbers = [12, -7, 9, -3, 25, 0, -14, 6, 8, -2]

try:
    index = int(input("Enter an index (0 to 9): "))
    value = numbers[index]
    if value > 0:
        print(f"The num at index {index} is positive.")
    elif value < 0:
        print(f"The num at index {index} is negative.")
    else:
        print(f"The num at index {index} is zero.")
except IndexError:
    print("Error: out of range.")
except ValueError:
    print("Error: enter a valid integer.")
