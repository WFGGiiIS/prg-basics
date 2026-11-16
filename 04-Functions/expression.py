def f(expression):
    total = 0
    current_number = ''
    current_operator = '+'
    for i in expression:
        if i.isdigit():
            current_number += i
        else:
            if current_number:
                if current_operator == '+':
                    total += int(current_number)
                elif current_operator == '-':
                    total -= int(current_number)
                current_number = ''
            current_operator = i
    if current_number:
        if current_operator == '+':
            total += int(current_number)
        elif current_operator == '-':
            total -= int(current_number)
    return total