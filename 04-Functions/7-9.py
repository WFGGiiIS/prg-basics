import sum

number = int(input("Enter a number: "))
is_even = input("Do you want sum of the even digits or odd digits (y/n): ")

print(f"The sum of the digits in {number} is: {sum.f(number, is_even)}")