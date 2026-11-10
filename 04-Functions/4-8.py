def time_string(hours, minutes, time_format):
    part_of_the_day = ''
    if time_format == '12':
        if hours > 12:
            part_of_the_day = 'pm'
            hours = hours - 12
        else:
            part_of_the_day = 'am'
        print(f'{hours}:{minutes}{part_of_the_day}')
    elif time_format == '24':
        hours = str(hours)
        minutes = str(minutes)
        if len(hours) == 1 and len(minutes) == 1:
            print(f"0{hours}:0{minutes}")
        else:
            print(f'{hours}:{minutes}')

hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))
time_format = input("Enter time format: ")
result = time_string(hours, minutes, time_format)
