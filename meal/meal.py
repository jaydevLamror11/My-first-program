def main ():
    time = convert(input("What time is it? "))

    # convert the inpupt.
    # if the time is between 7:00 to 8:00 OR 7:00 a.m. to 8:00 a.m. it's breakfast time.
    # if the time is between 12:00 to 13:00 OR 12:00 a.m. to 1:00 p.m. it's lunch time.
    # if the time is between 18:00 to 19:00 OR 6:00 p.m. to 7:00 p.m. it's dinner time.

    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")

def convert(time):
    # split the hours and minutes inputted by the user.
    # convert the hours and minutes into decimal/float values.
    # return the str to main.
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)/60
    tt = hours + minutes
    return tt

if __name__ == "__main__":
    main()

