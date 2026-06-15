
def emogi():
    face = input("heey: ")
    return face

def main():
    face = emogi()
    if face == "Hello :)":
        print("Hello 🙂")
    if face == "Goodbye :(":
        print("Goodbye 🙁")
    if face == ("Hello :) Goodbye :("):
        print("Hello 🙂 Goodbye 🙁")
main()

