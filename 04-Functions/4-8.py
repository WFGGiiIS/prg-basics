def time_string(hours, minutes, time_format):
    result = ''
    part_of_the_day = ''
    if time_format == '12':
        if hours > 12:
            part_of_the_day = 'pm'
            hours = hours - 12
        else:
            part_of_the_day = 'am'
        result = f"{hours}:{minutes}{part_of_the_day}"
        return result
    elif time_format == '24':
        hours = str(hours)
        minutes = str(minutes)
        if len(hours) == 1:
            result = f"0{hours}:{minutes}"
            return result
        else:
            result = f"{hours}:{minutes}"
            return result

hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))
time_format = input("Enter time format: ")
result = time_string(hours, minutes, time_format)

print(result)
