# convert decimal to octal number
print(oct(88))
# output:0o130


o_string = oct(155)
print(o_string)
# output:0o233


# *Note that the prefix “0o” that preceded the output indicates that the output is an octal number and can also be removed using:
# 	Using the string slicing format
o_string = oct(150)
print(o_string[2:])
# output:226


# Using the str.format() function
print('{0:o}'.format(200))
# output:310
