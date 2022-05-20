namesList = ['Daravuth', 'Sarapich', 'Theany', 'Kim hong']

print(namesList)
print(namesList[0])
print(namesList[len(namesList)-1])
print(namesList[-1])

# The insert method adds a new element to the list in the index specified
namesList.insert(1, 'Chhany')
namesList.insert(len(namesList)-1, 'Chatra')
print(namesList)

# The append method always adds the elements to the last index
namesList.append('Thearin')
print(namesList)

# The pop method will remove and return the last element in the list
# But if the index is passed then that particular element will be removed from the list
removedElement = namesList.pop()
print(namesList)
print(f"The element removed: {removedElement}")

# Count method will return the total number of occurrences of a particular element
print(namesList.count('Chatra'))

# Copy method will copy the elements of one list to another
# Copy method and = sign can be interchangeably be used
# May not be a very useful method
list1 = [12,51,45,8,98]
list2 = list1.copy()
# Same as list2 = list1
print(f'list 1: {list1}')
print(f'list 2: {list2}')

# Extend method will add the list items into another list
# list1.append(list2) this is wrong as it prints [num, [num]]
list1.extend(list2)
print(f'List 1: {list1}')

# The lists can be sorted with the help of sort method
# When sorting a list, elements has to be of same type
list2.sort()
print(list2)

# remove method will remove the element specified in the arguments

print(list2)
list2.remove(8)
print(list2)

# clear method will remove all the elements from the list

list2.clear()
print(list2)