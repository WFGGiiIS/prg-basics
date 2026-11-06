hours_parked = int(input("Enter how many hours the car was parked for: "))

if hours_parked == 1 or hours_parked == 2:
    print("That will be 5 PLN")
elif hours_parked >= 3 and hours_parked <= 6:
    print("That will be 15 PLN")
else:
    print("That will be 20 PLN") 