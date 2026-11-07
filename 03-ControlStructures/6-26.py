pin_code = '0805'
attempts = 0

while True:
    user_input = input("Enter the PIN code: ")
    if len(user_input) == 4 and user_input.isdigit():
        if user_input == pin_code:
            print("The PIN code is correct")
            break
        else:
            print("Incorrect...")
            attempts += 1
            if attempts == 3:
                print("Sorry, your payment card has been blocked")
                break
    else:
        print("It should contain only 4 numbers!")