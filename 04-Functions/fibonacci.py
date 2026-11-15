def f(n):
    index = 2
    first = 0
    second = 1
    while index < n:
        next_value = first + second
        index += 1
        first = second
        second = next_value
    return next_value