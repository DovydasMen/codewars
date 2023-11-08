def names_of_four_letters(friends: list) -> list:
    return [friend for friend in friends if len(friend) == 4]

print(names_of_four_letters(["Ryan", "Kieran", "Mark"]))