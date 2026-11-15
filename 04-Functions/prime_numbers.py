def f(n):
    prime_numbers = ''
    curr_number = 2
    found = 0

    while found < n:
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

    return prime_numbers.strip().split()[-1]