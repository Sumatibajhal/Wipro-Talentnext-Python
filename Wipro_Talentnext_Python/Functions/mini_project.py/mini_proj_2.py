'''
Create a Python module with the following functions:
Function Name
Task
ispalindrome(name)
Given the user name as input, this function should tell us whether the name is a palindrome or not.
count_the_vowels(name)
Given the user name as input, this function should tell us how many vowels are present in it.
frequency_of_letters(name)
Given the user name as input, this function should tell us how many times each letter appears in the name.
Note: name will be completely in either lower case or upper case.
Import the module in another python script and test the functions by passing appropriate inputs.
Sample input 1: bob
Sample output 1:
Yes it is a palindrome.
No of vowels: 1
Frequency of letters: b-2, 0-1
Sample input 2: marcel bentok tanaka
Sample output 2:
No it is not a palindrome.
No of vowels: 7
'''

import string_utils

def ispalindrome(name):
    cleaned_name = name.lower().replace(" ", "")  
    return "Yes it is a palindrome." if cleaned_name == cleaned_name[::-1] else "No it is not a palindrome."

def count_the_vowels(name):
    vowels = "aeiou"
    count = 0
    for char in name.lower():
        if char in vowels:
            count += 1
    return f"No of vowels: {count}"

def frequency_of_letters(name):
    frequency = {}
    for char in name.lower():
        if char.isalpha():
            frequency[char] = frequency.get(char, 0) + 1
 
    output_parts = []
    for char in sorted(frequency.keys()):
        output_parts.append(f"{char}-{frequency[char]}")
    return "Frequency of letters: " + ", ".join(output_parts)

print("Sample input 1: bob")
print(string_utils.ispalindrome("bob"))
print(string_utils.count_the_vowels("bob"))
print(string_utils.frequency_of_letters("bob"))
print("\n")

print("Sample input 2: marcel bentok tanaka")
print(string_utils.ispalindrome("marcel bentok tanaka"))
print(string_utils.count_the_vowels("marcel bentok tanaka"))
print(string_utils.frequency_of_letters("marcel bentok tanaka"))