def f(amount_to_pay):
    amount_of_coins = 0
    while amount_to_pay > 0:
        if amount_to_pay - 5 >= 0:
            amount_of_coins += 1
            amount_to_pay -= 5
        elif amount_to_pay - 2 >= 0:
            amount_of_coins += 1
            amount_to_pay -= 2
        elif amount_to_pay - 1 >= 0:
            amount_of_coins += 1
            amount_to_pay -= 1
    return amount_of_coins