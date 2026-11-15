def f(n):
    start = 1
    numbers_string = ''
    while start < n:
        numbers_string = numbers_string + str(start)
        start += 1
    numbers_string = numbers_string + str(n)
    return numbers_string