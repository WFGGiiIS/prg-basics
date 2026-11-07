e_n = int(input("Enter the number to convert: "))
starting_number = e_n
result = ''

while e_n > 1:
    if e_n % 2 == 0:
        result += '0'
        e_n = e_n / 2
    elif e_n % 2 != 0:
        result += '1'
        e_n = e_n / 2

if e_n == 1:
    result += '1'
result = result[::-1]
print(f"{starting_number} = {result}")