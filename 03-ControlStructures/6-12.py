products_bought = int(input("How many did you buy?: "))
product_price = 40

if products_bought > 2:
    total_price =  2 * 40 + ((products_bought - 2) * 40 * 0.75)
else:
    total_price = products_bought * 40

print(f"Amount to pay: {total_price}")