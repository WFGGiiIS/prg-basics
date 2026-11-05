###
# Calculates the sum of even numbers from 1 to a given number N
#
N = 10
n_counter = 0
sum_even = 0

while N != n_counter:
    n_counter += 1
    if n_counter % 2 == 0:
        sum_even += n_counter

print(f"The sum of even numbers from 1 to {N} is: {sum_even}")
