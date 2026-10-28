phone = input('Enter phone number (9-digits): ')
phone = phone[0:3] + '-' + phone[3:6] + '-' + phone[6:9]
print(phone)