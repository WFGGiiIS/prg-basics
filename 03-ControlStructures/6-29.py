n_numbers = int(input("How many prime numbers do you want?: "))

prime_numbers = ''
curr_number = 2
found = 0

while found < n_numbers:
    is_prime = True
    divisor = 2
    while divisor < curr_number:
        if curr_number % divisor == 0:
            is_prime = False
            break
        divisor += 1

    if is_prime:
        prime_numbers = prime_numbers + ' ' + str(curr_number)
        found += 1

    curr_number += 1

print(f"Prime numbers: {prime_numbers}")