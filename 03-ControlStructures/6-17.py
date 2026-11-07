hour24_format = input("Enter time (24-hour format): ")
hours = int(hour24_format[0:2])
minutes = int(hour24_format[3:5])

if hours < 12:
    part_of_the_day = 'am'
    print(f"Time in 12-hour format: {hours}:{minutes}{part_of_the_day}")
else:
    part_of_the_day = 'pm'
    print(f"Time in 12-hour format: {hours - 12}:{minutes}{part_of_the_day}")
