
def emoji():
    face = input("heey: ")
    return face

def main():
    face = emoji()
    if face == "Hello :)":
        print("Hello 🙂")
    if face == "Goodbye :(":
        print("Goodbye 🙁")
    if face == ("Hello :) Goodbye :("):
        print("Hello 🙂 Goodbye 🙁")
    else:
        print("I don't recognize that emoji text. ")
main()

