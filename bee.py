WORDS = {"HAIR": 4, "PAIR": 4, "CHAIR": 5, "GRAPHIC": 7}

def main():
    print("Welcome to spelling Bee!")
    print("Your letters are: A I P C R H G")

    while len(WORDS) > 0:
        print(f"{len(WORDS)} words left!")
        guess = input("Guess a word: "). upper()
    


        # TODO: check if guess in dictionaty
        if guess == "GRAPHIC":
            WORDS.clear()
            print("You have won the Game! ")
        elif guess in WORDS.keys():
            points = WORDS.pop(guess)
            print(f"Good job! You scored {points} points.")
        else:
            print("oops! Try again")
    for word, points in WORDS.items():
        print(f"{word} was worth {points} points.")

    print("That's the game!")

main()