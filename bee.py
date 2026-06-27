WORDS = {"HAIR": 4, "CHAIR": 4, "PAIR": 4}

def main():
    print("Welcome to spelling Bee!")
    print("Your letters are: A I P C R H G")

    while len(WORDS) > 0:
        print(f"{len(WORDS)} words left!")
        guess = input("Guess a word:")


        # TODO: check if guess in dictionaty

    print("That's the game!")

main()