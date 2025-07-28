'''
Project 4:
Given a string of n words, help Alex to find out how many times his name appears in the string.
Constraint: 1 <= n <= 200
'''

inp_string = "Hi Alex Welcome Alex Bye Alex."

words = inp_string.split()

count = 0
for word in words:
    count += word.count("Alex")

print("Number of times 'Alex' appears:", count)
