product_prize = float(input("Enter the product's prize: "))
discount = int(input("Enter the discount (%) for that product: "))
discount_converted = discount * 0.01
current_price = product_prize * discount_converted
difference = product_prize - current_price

print(f"Original price of the product is {round(product_prize, 2)} and its discount is -{discount}%")
print(f"Current price of the product with discount is {round(current_price, 2)}")
print(f"The difference in product's prizes is {round(difference, 2)}")