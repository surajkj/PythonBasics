# List functions
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

print(fruits.count('apple')) # Count of object

print(fruits.index('kiwi')) # Gives index of object.If multiple obj gives first index

fruits.reverse() #Reverse the given list
print(fruits)

fruits.append('grapes') # Append value at last position
print(fruits)

fruits.sort() # Sorts the list
print(fruits)

fruits.insert(4,'mango') # Insert object at given position
print(fruits)

fruits.remove('orange') # Removes given element
print(fruits)