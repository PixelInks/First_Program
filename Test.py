

mode = input("Welcome to the calculator. Enter 1 for addition and 2 for subtraction 3 for multiplication, 4 for division. ")
mode = int(mode)
if mode == 1: 
    x = input("Please type in your numbers.")
    y = input("Please type in your other number.")
    x = float(x)
    y = float(y)
    z = x+y
    print(z)
elif mode ==2:
    x = input("please type in  your number ")
    y = input("pleae type in your other number ")
    x = float(x)
    y = float(y)
    z = x-y
    print(z)
elif mode ==3:
    x = input("please type in  your number ")
    y = input("pleae type in your other number ")
    x = float(x)
    y = float(y)
    z = x*y
    print(z)
elif mode ==4:
    x = input("please type in  your number ")
    y = input("pleae type in your other number ")
    x = float(x)
    y = float(y)
    z = x/y
    print(z)
else:
    print ("Not a valid input. Bye!")