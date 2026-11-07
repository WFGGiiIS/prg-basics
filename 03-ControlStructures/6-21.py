amount = int(input("Enter the amount in PLN: "))
starting_amount = amount
pln1_coins = 0
pln2_coins = 0
pln5_coins = 0

while amount - 5 >= 0:
    pln5_coins += 1
    amount -= 5

while amount - 2 >= 0:
    pln2_coins += 1
    amount -= 2

while amount - 1 >= 0:
    pln1_coins += 1
    amount -= 1

print(f"The amount of PLN {starting_amount} in coins:")
print(f"5 PLN coins: {pln5_coins}")
print(f"2 PLN coins: {pln2_coins}")
print(f"1 PLN coins: {pln1_coins}")