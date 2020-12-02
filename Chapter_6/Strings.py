#Return a letter from a string
fruit="banana"
letter= fruit[0]
print(letter)

#Return the number of characters from a string
fruit = "banana"
print(len(fruit))

#Traversal with a While
index=0
while index<len(fruit):
    letter=fruit[index]
    print(letter)
    index=index+1

#Traversal with a For
for char in fruit:
    print(char)

#Return a slice [x:y] x is where it starts, y is how many characters you want(counting from the beginning)
#If you: 1) omit first index, starts at the beginning of the string, 2) omit second one, it will go to the end.
#If 1st index is > or = to 2nd index. Return blank.
s="MontyePython"
print(s[0:5])

fruit="banana"
print(fruit[:3])

print(fruit[3:])

#Count certain letters
word="banana"
count=0
for letter in word:
    if letter == "a":
        count=count+1
print(count)

#In operator = Boolean (True/False)
"a" in "banana"

#String comparison (Beware uppercase letters will return before lowercase letters)
word=input("Enter word: \n")
if word == "banana":
    print("All right, bananas")

word=input("Enter word: \n")
if word < "banana":
    print("Your word,"+word+", comes before banana")
elif word > "banana":
    print("Your word," + word + ", comes after banana")
else:
    print("All right, bananas!")
