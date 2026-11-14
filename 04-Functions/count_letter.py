def count_letter(message, letter):
    count = 0
    for i in message:
        if i == letter:
            count += 1
    return count