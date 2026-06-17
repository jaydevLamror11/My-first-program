
uni = input("What is the answer to the great question of life , the Universe, and everythin? ")

match uni:
    case "42" | "Forty Two" | "forty_two":
        print ("yes! 🙂")
    case _:
        print("noo 🙁")
