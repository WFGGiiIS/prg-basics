def f(number):
    number = str(number)
    sum = 0
    for i in number:
        x = number.count(i)
        if x > 1:
            sum += int(i)
    return sum