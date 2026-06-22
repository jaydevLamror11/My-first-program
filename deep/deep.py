uni = input("What is the answer to the great question of life , the Universe, and everythin? ")
uni = uni . strip() . lower()

if uni == "42":
    print("Yes")
elif uni == "Forty Two":
    print("Yes")
elif uni == "forty-two":
    print("Yes")
elif uni == "forty two":
    print("Yes")
elif uni == " FoRty TwO":
    print("Yes")
else:
     print("No")

