'''
Write a Python function that accepts a hyphen-separated sequence of colors as input and returns the colors in a hyphen-separated sequence after sorting them alphabetically.
Constraint: All the colors will be completely in either lower case or upper case.
'''
def sort_colors(color_sequence):
    colors = color_sequence.split('-')
    sorted_colors = sorted(colors)
    return '-'.join(sorted_colors)
input1 = "green-red-yellow-black-white"
input2 = "PINK-BLUE-TAN-PURPLE"

print("Sorted colors:", sort_colors(input1))
print("Sorted colors:", sort_colors(input2))  
