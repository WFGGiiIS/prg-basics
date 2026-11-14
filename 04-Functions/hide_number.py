def hide(card_number):
    new_card_number = ''
    index = 0
    for i in card_number:
        index += 1
        if index > 2 and index < 13:
            new_card_number = new_card_number + '*'
        else:
            new_card_number = new_card_number + i
    return new_card_number