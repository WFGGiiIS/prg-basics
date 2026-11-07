x = int(input("Enter first coordinate x: "))
y = int(input("Enter second coordinate y: "))

if x > 0 and y > 0:
    print(f"Point P({x},{y}) is in first quadrant of the coordiane system")
elif x < 0 and y > 0:
    print(f"Point P({x},{y}) is in second quadrant of the coordiane system")
elif x < 0 and y < 0:
    print(f"Point P({x},{y}) is in third quadrant of the coordiane system")
elif x > 0 and y < 0:
    print(f"Point P({x},{y}) is in fourth quadrant of the coordiane system")
elif x == 0:
    print(f"Point P({x},{y}) is located on y axis")
elif y == 0:
    print(f"Point P({x},{y}) is located on x axis")
else:
    print(f"Point P({x}, {y}) is located in the position (0,0) of the coordinate system")