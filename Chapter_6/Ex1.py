#Backward traversal with While
fruit="banana"
index=(len(fruit)-1)
while index >= 0:
    letter=fruit[index]
    print(letter)
    index=index-1