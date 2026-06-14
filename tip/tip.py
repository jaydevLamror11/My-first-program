
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")



def dollars_to_float(d):
    a = float(d.strip("$"))
    return a


def percent_to_float(p):
    b = float(p.strip("%"))*float(0.01)
    return b
main()
