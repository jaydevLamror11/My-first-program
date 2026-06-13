def universe():
    uni = input("What is the answer to the great question of life , the Universe, and everythin? ")
    return uni


def main():
     uni = universe()
     if uni == '42':
         print("yes! 🙂")
     else:
         print("no 🙁")


main()