#Write a function that accepts a string and prints the number of upper case letters and lower case letters in it.
def casecheck(inp_string):
    upper_count = 0
    lower_count = 0

    for char in inp_string:
        if 'A' <= char <= 'Z':
            upper_count += 1
        elif 'a' <= char <= 'z':
            lower_count += 1
    return upper_count, lower_count

str1 = 'Hello World'
print(casecheck(str1))