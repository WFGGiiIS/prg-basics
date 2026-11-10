def sum_digits(number):
    total = 0
    number = abs(number)
    number = str(number)
    for i in number:
        i = int(i)
        total += i
    return total

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')