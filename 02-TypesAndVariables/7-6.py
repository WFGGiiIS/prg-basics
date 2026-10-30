car_speed = int(input("Enter vehicle speed: "))
police_radar = car_speed >= 40 and car_speed <= 140

print(f"Speed is valid: {police_radar}")