dogs_age = int(input("Enter your dog's age: "))

if dogs_age <= 2:
    in_human_years = dogs_age * (10.5 / 2)
else:
    in_human_years = dogs_age * 4

print(f"Your dog is {in_human_years} in human years")