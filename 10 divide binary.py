binary_1 = input('enter the first binary number:')
binary_2 = input('enter the second binary number:')
result = int(binary_1, 2) // int(binary_2, 2)
reminder = int(binary_1, 2) % int(binary_2, 2)
result = bin(result)
reminder = bin(reminder)
print("{r} R {m}".format(r=result, m=reminder))
