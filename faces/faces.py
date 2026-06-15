
def emoji():
    face = input("heey: ")
    return face

def main():
    face = emoji()
    if face == "Hello :)":
        print("Hello 🙂")
    elif face == "Goodbye :(":
        print("Goodbye 🙁")
    elif face == ("Hello :) Goodbye :("):
        print("Hello 🙂 Goodbye 🙁")
    else:
        print("I don't recognize that emoji text. ")
main()

