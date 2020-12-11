# Create a list
cheeses = ['Cheddar', 'Edam', 'Gouda']
numbers = [17, 123]
empty = []
print(cheeses, numbers, empty)
print(cheeses[1])

# Reassign an item in a list
numbers = [17, 123]
numbers[1] = 5
print(numbers)

t = ['a', 'b', 'c', 'd', 'e']
t[1:3] = ['x', 'y']
print(t)

# In Operator in a List
cheeses = ['Cheddar', 'Edam', 'Gouda']
print('Edam' in cheeses)

# Len = Number of elements in a list
cheeses = ['Cheddar', 'Edam', 'Gouda']
print(len(cheeses))

# If a list contains a nested list inside, it still count as 1 element
list = ['spam',1,['Brie', 'Roquefort', 'Pol le Veq'], [1,2,3]]
print(len(list))

# Traversing a list and updating values
numbers = [5, 7, 15]
for i in range (len(numbers)):
    numbers[i] = numbers[i]*2
print(numbers)

# A for loop over an empty list never executes the body
empty = []
for x in empty:
    print ("This wont print")

# List Operations (Sum = Concatenates a list)
a = [1,2,3]
b = [4,5,6]
c = a+b
print(c)

# List Operations ( * = Repeats a list)
a = [1,5]
b = a*3
print(b)

# Since list are mutable, it is useful to make a copy before performing operations

# Slice in a List
t = ['a', 'b', 'c', 'd', 'e']
print(t[1:3])

# List Methods
# list.append() - Adds a new element to the end of a list
# list.extend() - Takes a list as an argument and append all the elements
# list.sort()   - Arranges the elements of the list from low to high

t = ['a', 'b', 'c']
t.append('d')
print(t)

t1 = ['a', 'b', 'c']
t2 = ['d', 'e']
t1.extend(t2)
print(t1)

t = ['d', 'c', 'e', 'b', 'a']
t.sort()
print(t)

#Deleting elements

