def f(password):
    check_string = ''
    for i in password:
        if i not in check_string:
            check_string = check_string + i
    return len(check_string) >= 6 and len(check_string) == len(password)