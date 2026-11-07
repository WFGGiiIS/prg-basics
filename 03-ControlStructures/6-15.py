EAN_num = input("Enter EAN-13 article number: ")

if len(EAN_num) == 13 and EAN_num.isdigit():
    print("Article number is correct")
    if EAN_num[0:3] == '590':
        print("Article manufactured in Poland")