# request that user input an octal number
octal_number = input('Enter an Octal number: ')
# initialize the decimal number
decimal = 0
# length of octal input
length_of_number = len(octal_number)
# loop through each digit of the octal number
for x in octal_number:
    # decrease length_of_number by 1
    length_of_number = length_of_number-1
    # multiplication
    decimal += pow(8, length_of_number) * int(x)
print("Decimal of {p} is {q} ".format(p=octal_number, q=decimal))
