yoo = input("Expression: ")
a, b, c = yoo.split(" ")
a = float(a)
c = float(c)

if b == "+":
    print(round(a+c,1))
elif b == "-":
    print(round(a-c,1))
elif b == "*":
    print(round(a*c,1))
elif b == "/":
    print(round(a/c,1))
