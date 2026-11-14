import all_checkers

given_number = int(input("Give a number: "))
x_value = int(input("Give a starting range point: "))
y_value = int(input("Give an end range point: "))

check = all_checkers.is_in_range(x_value, y_value, given_number)

print(f"Number {given_number} in the range <{x_value},{y_value}>: {check}")