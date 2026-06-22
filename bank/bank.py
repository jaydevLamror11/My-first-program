
yoo = input("Greeting: ")
yoo = yoo . strip()

match yoo:
    case "Hello" | "Hello, Newman":
        print ("$0")
    case "How you doing?":
        print("$20")
    case _:
        print("$100")
