def main():
    names = ["Mario", "Luigi", "Daisy", "Yoshi"]
    for i in range(len(names)):
                   print(write_letter(names[i], "Princess Peach"))

def write_letter(reciever, sender):
    return f"""
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Dear {reciever},

        You are conrdially invited to a ball at 
        Peach's Castle this evening, 7:00 PM.

        Sincerely,
        {sender}
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """

main()