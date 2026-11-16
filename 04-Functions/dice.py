def f(dice):
    if dice.isdigit():
        longest_streak = 1
        current_streak = 1
        current_number = dice[0]
        best_number = int(dice[0])
        for i in range(1, len(dice)):
            if dice[i] == current_number:
                current_streak += 1
            else:
                if current_streak > longest_streak:
                    longest_streak = current_streak
                    best_number = int(current_number)
                current_number = dice[i]
                current_streak = 1
        if current_streak > longest_streak:
            longest_streak = current_streak
            best_number = int(current_number)
        return best_number

print(f("5233165554211"))
        