import negative_finder

x_value = int(input("Give a starting range point: "))
y_value = int(input("Give an end range point: "))

print(f"The number of negative numbers in the given range <{x_value},{y_value}> is: {negative_finder.f(x_value, y_value)}")