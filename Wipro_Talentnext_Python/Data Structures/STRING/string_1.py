#Write a program to count the number of upper and lower case letters in a String.

upper_count = 0
lower_count = 0
str1 = 'Hello World'
for char in str1:
    if 'A' <= char <= 'Z':
        upper_count += 1
    elif 'a' <= char <= 'z':
        lower_count += 1
print(f"Number of Upper case letters: {upper_count} and Lower case letters: {lower_count}")




