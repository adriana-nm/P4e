# Return a letter from a string
fruit = "banana"
letter = fruit[0]
print(letter)

# Return the number of characters from a string
fruit = "banana"
print(len(fruit))

# Last character is -1. The previous one is -2, and so on.

# Traversal with a While
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1

# Traversal with a For
for char in fruit:
    print(char)

# Return a slice [x:y] x is where it starts, y is how many characters you want(counting from the beginning)
# If you: 1) omit first index, starts at the beginning of the string, 2) omit second one, it will go to the end.
# If 1st index is > or = to 2nd index. Return blank.
s = "MontyePython"
print(s[0:5])

fruit = "banana"
print(fruit[:3])

print(fruit[3:])

# Count certain letters
word = "banana"
count = 0
for letter in word:
    if letter == "a":
        count = count + 1
print(count)

# In operator = Boolean (True/False)
"a" in "banana"

# String comparison (Beware uppercase letters will return before lowercase letters)
word = input("Enter word: \n")
if word == "banana":
    print("All right, bananas")

word = input("Enter word: \n")
if word < "banana":
    print("Your word," + word + ", comes before banana")
elif word > "banana":
    print("Your word," + word + ", comes after banana")
else:
    print("All right, bananas!")

# String methods more used

# str.find()  - Find the position of a substring ( if the substring is not found it returns -1).
#               You can put the position where it starts to look for the substring ("text", position).
#               Usually we convert everything to lower case first.
# str.capitalize() - Capitalize the first letter of the string
# str.upper() - Transform all the string in upper case
# str.lower() - Transform all the string in lower case
# str.replace()- Like search and replace.
#               It replace all the occurrences of the search string with the new replacement string.
# str.lstrip()- Remove whitespace at the left side (start)
# str.rstrip()- Remove whitespace at the right side (end)
# str.strip() - Remove both beginning and ending whitespace
# str.startswith() - Prefixes. Boolean (True/False) if starts with certain substring
# str.endswith()- Suffixes. Boolean (True/False) if ends with certain substring
# str.center() - Will center align the string. The character I declare will fill the extra spaces.
#    .join() - It will join my string, separated by the text I declare before the join
# str.punctuation - Show the characters that are considered as punctuation.

fruitnew = "Manzana"
text = fruitnew.find("na", 3)
print(text)

notfruit = "tomate"
newnotfruit = notfruit.capitalize()
print(newnotfruit)

fruitnew = "Manzana"
textupper = fruitnew.upper()
print(textupper)

fruitnew = "Manzana"
textlower = fruitnew.lower()
print(textlower)

greet = "Hello Bob"
greetnew = greet.replace("o","x")
print(greetnew)

greetspace= "   Hello Bob   "
print(greetspace.lstrip())

greetspace= "   Hello Bob   "
print(greetspace.rstrip())

greetspace= "   Hello Bob   "
print(greetspace.strip())

line = "Please have a nice day"
print (line.startswith("P"))

line = "Please have a nice day"
print (line.endswith(("a","b")))

fruit = "banana"
center = fruit.center(12,"O")
print (center)

myTuple = ("John", "Peter", "Vicky")
x = "-".join(myTuple)
print(x)

import string
print(string.punctuation)

#Parsing Strings (look into a string and find inside a substring and extract it)
data = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
atpos = data.find("@")
sppos = data.find(" ", atpos)
host = data[atpos+1 : sppos]
print (host)

# Format Operator

# %s - String (or any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers (default 6 digits)
# %g - Floating point format
# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

name = "Jhon"
age = 23
print ("%s is %d years old" % (name, age) )

mylist = [1,2,3]
print ( "A list: %s" % mylist)

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s"
print(format_string % data)
