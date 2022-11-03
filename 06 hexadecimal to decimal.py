conversion_table = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
                    '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

hexadecimal_number = input("Enter hexadecimal number: ").strip().upper()
# initialisation
decimal_number = 0
# computing max power value
power = len(hexadecimal_number) - 1
for digit in hexadecimal_number:
    decimal_number += conversion_table[digit]*16**power
    power -= 1
print(decimal_number)
