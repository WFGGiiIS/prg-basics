def f(number, even):
    number = str(number)
    sum_of_the_digits = 0
    if even == 'y':
        for i in number:
            if int(i) % 2 == 0:
                sum_of_the_digits += int(i)
        return sum_of_the_digits
    else:
        for i in number:
            if int(i) % 2 != 0:
                sum_of_the_digits += int(i)
        return sum_of_the_digits
