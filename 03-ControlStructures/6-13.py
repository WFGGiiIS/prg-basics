car_speed = int(input("Enter your vehicle's speed: "))
speed_limit_max = 140
speed_limit_min = 40

if car_speed < speed_limit_min:
    print("Warning: invalid car speed!!")
elif car_speed > speed_limit_max:
    print("Warning: too fast!!!")