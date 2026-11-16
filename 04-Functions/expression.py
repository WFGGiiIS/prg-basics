def f(expression):
    count = 0
    result = 0
    while count < len(expression):
        for i in expression:
            if i == "+":
                if result == 0:
                    i_index = expression.index(i)
                    first_num = int(expression[count-i_index])
                    second_num = int(expression[count+i_index])
                    print(first_num, second_num)
                    result += first_num + second_num
                else:
                    i_index = expression.index(i)
                    result += i_index
            elif i == "-":
                if result == 0:
                    i_index = expression.index(i)
                    first_num = int(expression[count-i_index])
                    second_num = int(expression[count+i_index])
                    result -= first_num - second_num
                else:
                    i_index = expression.index(i)
                    result -= i_index
            count += 1
    return result
print(f("2+3-4+5-0"))