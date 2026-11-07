first_term = 0
second_term = 1
total_numbers = ''
total_numbers = total_numbers + '' + str(first_term) + ' ' + str(second_term)

for i in range(1, 21):
    sub_term = first_term + second_term
    total_numbers = total_numbers + ' ' + str(sub_term)
    i += 1
    first_term = second_term
    second_term = sub_term

print(total_numbers)