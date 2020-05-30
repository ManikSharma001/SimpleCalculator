#Simple Calculator with Python
def addition(numOne, numTwo):
    return (numOne + numTwo)

def subtraction(numOne, numTwo):
    return(numOne - numTwo)

def multiplication(numOne, numTwo):
    return(numOne * numTwo)

def division(numOne, numTwo):
    return(numOne / numTwo)

response = ""
while response != "n".lower():
    print("What is the First Number?")
    fnum = float(input())
    print("What Operation would you like to perform?")
    operation = input()
    print("What is the Second Number?")
    snum = float(input())

    if operation[0].lower() == "a":
        addition(fnum, snum)
    elif operation[0].lower() == "s":
        subtraction(fnum, snum)
    elif operation[0].lower() == "m":
        multiplication(fnum, snum)
    else:
        division(fnum, snum)
    print("Would You Like to Continue with this Answer (Press 'n' for no)?")
    response = input()
