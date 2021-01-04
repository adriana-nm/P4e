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

# In Operator in a List (IN results in a Boolean)
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

#DELETING ELEMENTS

#POP - Delete an item and saved it in a variable (no index, it deletes the last one)
t=['a', 'b', 'c']
x = t.pop(1)
print(t)
print(x)

t=['a', 'b', 'c']
x = t.pop()
print(t)
print(x)

#DEL - Delete an item (need the index/position)

t = ['a', 'b', 'c']
del t[1]
print(t)

t = ['a', 'b', 'c','d','e','f']
del t[1:5]
print(t)

#REMOVE - If finds and delete a value (if you dont know the index)

t = ['a', 'b', 'c']
t.remove('b')
print(t)

#FUNCTIONS

# len - Return the quantity of values/items
# max - Return the max. value
# min - Return the min. value
# sum - Return sum the values. It only works when the elements are numbers.

nums= [3,41,12,9,74,15]
print (len(nums))

nums= [3,41,12,9,74,15]
print (max(nums))

nums= [3,41,12,9,74,15]
print (min(nums))

nums= [3,41,12,9,74,15]
print (sum(nums))

nums= [3,41,12,9,74,15]
print (sum(nums)/len(nums))

numlist = list()
while (True):
    inp = input ('Enter a number: ')
    if inp=='done': break
    value = float(inp)
    numlist.append(value)
average= sum(numlist) / len(numlist)
print('Average: ',average)

#STRINGS

# List - Convert a string into a list of characters.

s = 'spam'
t = list(s)
print(t)

# Split - Divide a string into words

s = 'what a nice function'
t = s.split()
print(t)
print(t[2])

# Delimiter - Split a string with a delimiter character.

s = 'spam-spam-spam'
delimiter = '-'
print(s.split(delimiter))

# Join - It takes a list of strings and concatenates the elements

t = ['what','a','nice','function']
delimiter = ' '
print(delimiter.join(t))

#PARSING

#Extracting the Day of a list of enails
#Example mail: From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    print(words[2])

# OBJECTS AND VALUES

# 2 list with the same value is not the same object
a = [1,2,3]
b = [1,2,3]
print(a is b)

#ALIASING

# Asigning a same object (Reference = Association of a variable with an object)
a = [1,2,3]
b = a
print(b is a)

# Object with more than 1 reference is aliased.
# Aliased objects are mutable, changes in 1 alias affect the other
a = [1,2,3]
b = a
b[0] = 17
print(a)

# Avoid aliasing with mutable objects
# Strings are inmutable objects, so not much problem

#LIST ARGUMENTS


