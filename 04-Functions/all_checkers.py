def is_in_range(x, y, n):
    if n >= x and n <= y:
        return True
    else:
        return False

def f(binary_number):
    count = 0
    for i in binary_number:
        if i == "0" or i == "1":
            count += 1
    if count == len(binary_number):
        return True
    else:
        return False