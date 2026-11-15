def f(n):
    count = 0
    asterisks_string = ''
    if n > 1:
        while count < n:
            if n == count + 1:
                asterisks_string = asterisks_string + "*"
            else: 
                asterisks_string = asterisks_string + "*" + "/"
            count += 1
        return asterisks_string
    else:
        return "*"