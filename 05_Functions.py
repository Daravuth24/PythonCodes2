def addTwoNumbers():
    num1 = int(input("Enter number: "))
    num2 = int(input("Enter number: "))
    print("The sum is: ", (num1 + num2))
    # print(f"Sum = ${num1 + num}") 

def subtractTwoNumbers():
    num1 = int(input("Enter number: "))
    num2 = int(input("Enter number: "))
    print("Difference = ", (num1 - num2))

def multiplyTwoNumbers():
    num1 = int(input("Enter number: "))
    num2 = int(input("Enter number: "))
    print("Product = ", (num1 * num2))

def divTwoNumbersFindQuotient():
    num1 = int(input("Enter number: "))
    num2 = int(input("Enter number: "))
    print("Division = ", (num1 // num2))

def divTwoNumbersFindRemainder():
    num1 = int(input("Enter number: "))
    num2 = int(input("Enter number: "))
    print("Difference = ", (num1 % num2))

choice = int(input("Input your choice of operations\n1. Addition\n2. Subtraction\n3."
                   " Multiplication\n4. Division(Quotient)\n5. Division(Remainder)\nYour choice: "))
if choice == 1:
    addTwoNumbers()
elif choice == 2:
    subtractTwoNumbers()
elif choice == 3:
    multiplyTwoNumbers()
elif choice == 4:
    divTwoNumbersFindQuotient()
elif choice == 5:
    divTwoNumbersFindRemainder()
