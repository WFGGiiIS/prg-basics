current_price = 140
previous_price = 200
sale = ((previous_price - current_price) / previous_price) * 100

if sale > 10:
    print("Buy the prodcut!!!")
    print(f"Product price reduced by {sale}%")