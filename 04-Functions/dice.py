def f(dice):
    max_rolled = 0
    highest_num = 0
    extra_v = 0
    for i in dice:
        if extra_v == i:
            if highest_num < int(i):
                highest_num = int(i)
                max_rolled += 1
            print(max_rolled, highest_num)
        else:
            extra_v = i
    return highest_num

print(f("523316554211"))
        