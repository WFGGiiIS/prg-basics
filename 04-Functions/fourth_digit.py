def f(product_code):
    if len(product_code) == 4 and product_code.isdigit(): 
        fourth_digit = 0
        sum = 0
        three_digits = product_code[0:3]
        for i in three_digits:
            sum += int(i)
        fourth_digit = sum % 7
        return fourth_digit == int(product_code[3:4])
    else:
        return TypeError("ERROR: THE CODE MUST CONSIST ONLY NUMBERS!")