#Functions are defined here
def add(firstNumber, secondNumber):
    x = firstNumber+secondNumber
    return x

def sub(firstNumber, secondNumber):
    y = firstNumber-secondNumber
    return y

def multi(firstNumber, secondNumber): 
    z = firstNumber*secondNumber
    return z

def div(firstNumber, secondNumber): 
    c = firstNumber/secondNumber
    return c

#Program starts here
mode = input("Welcome to the calculator. Enter 1 for addition and 2 for subtraction 3 for multiplication, 4 for division. ")
mode = int(mode)

a = float(input("please enter your first number "))
b = float(input("please enter your second number "))

if mode == 1:
    output = add(a,b)
    print (output)
elif mode == 2:
    output = sub(a,b)
    print (output)
elif mode == 3:
    output = multi(a,b)
    print (output)
elif mode == 4:
    output = div(a,b)
    print (output)
else:
    print ("Have a nice day")