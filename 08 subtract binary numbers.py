binary_1 = input('enter the first binary number:')
binary_2 = input('enter the second binary number:')
sub = int(binary_1, 2) - int(binary_2, 2)
sub = bin(sub)
print(sub)
