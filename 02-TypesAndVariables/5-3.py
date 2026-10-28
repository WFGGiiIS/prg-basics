a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
volume = a * b * c
surface_area = 2 * (a * b + b * c + a * c)

print(f"The cuboid with sides {a}, {b}, {c} has volume of {volume} and surface area of {surface_area}")