# Tuples are not modifiable.
myTuple = (20,30,45,54,54,65, "test", "test1")
myTuple1 = (20,30,45,54,54,65)
myList = [20,20,40]

print("Tuple elements: ", myTuple)
print("Length of Tuple: ", len(myTuple))

print(f"The index of 45: {myTuple.index(45)}")

print("Tuple elements: ", myTuple)

print(f"The total elements in the tuple are: {myTuple.count(54)}")
print(f"The total elements in the tuple are: {myTuple.count('test')}")

print(f"The maximum element in the tuple is: {max(myTuple1)}")
print(f"The minimum element in the tuple is: {min(myTuple1)}")

myTuple2 = tuple(myList)
myList2 = list(myTuple)
print(type(myTuple2))
print(type(myList2))
