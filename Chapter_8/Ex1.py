# Write a function called chop, takes a list and modifies it.
# Removes the first and last elements, and returns None.
def chop(t):
    del t[::len(t)-1]
    print(t)

def chop2(t):
    del t[len(t)-1]
    del t[0]
    print(t)

def chop3(t):
    del t[-1]
    del t[0]
    print(t)

list = ['4','5','8','1','7']
chop2(list)



# Write a function called middle, takes a list and returns a new list.
# New list contains all but the first and last elements.

def middle(t):
    newlist = t[1:len(t)-1]
    print(newlist)

list = ['4', '5', '8', '1', '7']
middle(list)