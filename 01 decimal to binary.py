# this method print the binary equivalent of 100
print(bin(100))
#output: 0b1100100

# Alternatively:
# Program that also print the binary equivalent of decimal number

b_string = bin(120)
print(b_string)
#output: 0b1111000

# Use the string slicing method or the str.format() function as follows to remove the prefix 0b from the output: Using the string slicing format
b_string = bin(100)
print(b_string[2:])
# output:1100100

# Using the str.format() function
print('{0:b}'.format(128))
# output:10000000
