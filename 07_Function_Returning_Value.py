# def getName1():
    # print("This is a function with return value")
    # return "Masaki"
# returnedValue = getName1()
# print(returnedValue)

def getName():
    # print("This is a function with return value")
    name = input("Enter your name:")
    return name

# returnedValue = getName()
# print(f"Welcome: {returnedValue}")

def getNameAndConvertToLowerCase():
    name = input("Enter your name to be converted into lower case:")
    convertedName = name.lower()
    return convertedName

# returnedName = getNameAndConvertToLowerCase()
# print(returnedName)

def getNameAndConvertToUpperCase():
    return input("Input your name to be converted into uppercase: ").upper()

print(getNameAndConvertToUpperCase())