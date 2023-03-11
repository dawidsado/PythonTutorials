import math


def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()

a = input("pick a")
b = input("pick b")
c = input("pick c")

if not check_int(a) or not check_int(b) or not check_int(c):
    print("incorrect value")
else:
    a = int(a)
    b = int(b)
    c = int(c)
    delta = (b**2)-(4*a*c)
    print("delta is:", delta)
    if delta < 0:
        print("Error, there is no solutions")
    elif a == 0:
        print("That's not square equation")
    elif delta == 0:
        print("x1 is: ", (-b/2*a))
    elif delta > 0:
        print("x1 and x2: ", (-b-delta**0.5)/(2*a), (-b+delta**0.5)/(2*a))



