# convert decimal to octal number
print(hex(230))
# output:0xe6


x_string = hex(159)
print(x_string)
# output:0x9f


# *Note that the prefix 0o that preceded the output indicates that the output is an octal number and can also be removed using:
# Using the string slicing format
o_string = hex(190)
print(o_string[2:])
# output:be


# ii. Using the str.format() function
print('{0:x}'.format(247))
# output:f7
