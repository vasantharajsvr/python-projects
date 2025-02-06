import calcalator
def equal(num1,num2):
    return num1 == num2

def notequal(num1,num2):
    return num1 != num2

def greaterthan(num1,num2):
    return num1 > num2

def lessthan(num1,num2):
    return num1 < num2

def greaterthanequal(num1,num2):
    return num1 >= num2

def lessthanequal(num1,num2):
    return num1 <= num2

print("select a operator -\n"\
    "1.equal\n" \
    "2.notequal\n" \
    "3.greaterthan\n" \
    "4.lessthan\n" \
    "5.greaterthanequal\n" \
    "6.lessthanequal\n")

select = int(input("enter your choice 1,2,3,4,5,6 "))

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

if select == 1:
    print(equal(number1, number2))

elif select == 2:
    print( notequal(number1, number2))

elif select == 3:
    print(greaterthan(number1, number2))

elif select == 4:
    print(lessthan(number1, number2))

elif select == 5:
    print( greaterthanequal(number1, number2))

elif select == 6:
    print(lessthanequal(number1, number2))

else:
    print("Invalid input")