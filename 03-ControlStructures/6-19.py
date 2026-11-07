first_q = input("SURVEY Are you interested in computer science? (y/n): ")
second_q = input("Do you like playing computer games? (y/n): ")
third_q = input("Do you have an instgram account? (y/n): ")

if first_q == 'y':
    result1 = 'Yes'
else:
    result1 = 'No'

if second_q == 'y':
    result2 = 'Yes'
else:
    result2 = 'No'

if third_q == 'y':
    result3 = 'Yes'
else:
    result3 = 'No'

print(f"SURVEY RESULTS Interested in computer science: {result1}")
print(f"Playing computer games: {result2}")
print(f"Has an Instagram account: {result3}")