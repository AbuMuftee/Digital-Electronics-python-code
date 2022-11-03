# python program to convert binary number
# to it decimal equivalent

# you are requested to enter a binary number
binary_number = list(input('enter a binary number:'))
number = 0  # initialization
for i in range(len(binary_number)):
    # iteration for the length of the binary number
    figure = binary_number.pop()  # pop the next binary digit
    if figure == '1':  # the next operation is only performed on digit 1
        number = number+pow(2, i)
print('the decimal equivalent of the number is', number)
