# Tuples: Tuples are used to store multiple items in a single variable.
# Inmutable: Once a tuple is created, you cannot change its values.
# Comparable: You can compare 2 tuples and get a true/false response.
# Hashable: You can put them through the function Hash and get a number.
# Tuples are more efficient in terms of memory use and performance than a list.
# When you make "temporary variables" is preferable to use tuples over list.



# Parenthesis: Not necesary but used to quicly identify a tuple
t = ('a','b','c','d','e')

# CREATE a tuple
# 1) If you put a single element, put a coma at the end. Otherwise it will take the data as string.
# 2) Use the built-in function tuple. If you put data, put 2 parenthesis.
t1 = ('a',)
print(type(t1))

t = tuple()
print(t)

t = tuple(('apple','banana','cherry'))
print(t)

# If the argument is a sequence (string, list or tuple), the result of a call
# of a tuple, is a tuple with this elements of the sequence.
t = tuple('lupins')
print(t)              # Return ('l','u','p','i','n','s')

# Most list operators work also with tuples.
# *Bracket to call with an index print(t[0])
# *Slice operator selecting a range of elements print(t[1:3])

# MODIFY. Cannot modify the elemnts of the tuple. You get an error.
# But you can replace one tuple with another
t = ('a','b','c','d','e')
t =('A',) + t[1:]
print(t)

# Or you can convert theh tuple into a list, change the list and conver it back to tuple.
x = ('apple','banana','cherry')
y = list(x)
y[1] = 'kiwi'
x = tuple(y)
print(x)

# YOU ALSO CANNOT: sort, append items, reverse, etc. Any action that modifies the tuple is not allowed.

# Tuple Methods
t = list()
print(dir(t))

# tuple.count() - Return the # of times an element appears on the list
# tuple.index() - Find the element searched, and return the position. If it's not on the list returns an error.
t = ('b', 'c', 'e', 'b', 'a')
print(t.count('b'))
print(type(t))

t = ('b', 'c', 'e', 'b', 'a')
print(t.index('e'))
print(type(t))

# TUPLE ASSIGNMENT

# Assign tuples to several variables
(x,y) =(4,'Fred')
print(y)

# Invert the value of the tuples
m = ('have', 'fun')
x,y = m
print('m:',m)
print('x:',x)
print('y:',y)
print(type(m))
x,y = y,x
print('x:',x)
print('y:',y)

# Ex. Divide a string and assign parts of that string to variables.
addr = 'monty@python'
uname,domain = addr.split('@')
print(uname)
print(domain)
print(type(uname))

# DICTIONARIES AND TUPLES

# Items() method in dictionaries returns a list of tuples.
d = dict()
d['csev'] = 2
d['cwen'] = 4
for (k,v) in d.items():  # (k,v) is a tuple, but k is string and v is integer
    print(k,v)
tups = d.items()
print(tups)

d = {'a':10, 'b':1, 'c':22}
t = list(d.items())
print(t)

# COMPARING TUPLES
# It will check the tuples in order. First the 1st item on the left.
# If the 1st item is equal, it will go to the second item (until 1 provides a result)
# If an item provides a result (>,<) it will give a result (true/false) and it will stop.
# Once you get a result it won't check the other items

(0,1,2)<(5,1,2)         # 0 less than 5, true.
(0,1,2000000)<(0,3,4)   # 0 less than 0, no result. 1 < 3, true. It doesnt check the 3rd number
('Jones','Sally')<('Jones','Sam') # jones less joness, no result. l < m, true

# Comparing tuples allows us to SORT IT.
# You can sort a dictionary using tuples.
# SORT BY KEY  ( with sorted() or create a list and then list.sort() )
d = {'b':1,'a':10,'c':22}
print(d.items())
print(sorted(d.items()))  # It will sort the list of tuples, by ordering the keys.

d = {'b':1,'a':10,'c':22}
for k,v in sorted(d.items()):
    print(k,v)

# SORT BY VALUE
c = {'a':10,'b':1,'c':22}
tmp = list()
for k,v in c.items():
    tmp.append((v,k))  # or you could create a new tuple and then append to the list
    tmp =sorted (tmp)  # or you could use just: tmp.sort()
print(tmp)
# if you want to sort backwards you use: tmp.sort(reverse=True) / tmp = sorted(tmp, reverse=True)

# Ex. Print the top 10 most common words
# Use r before the file location, to convert to raw string. Or use \\ (in all the line) instead of \.
fhand = open(r'C:\Users\adri_\PycharmProjects\P4E\romeo-full.txt','r')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1
lst = list()
for key,val in counts.items():
    newtup = (val,key)
    lst.append(newtup)
lst = sorted(lst,reverse=True)
for val,key in lst[:10]:
    print(key,val)

# List Comprehension:  Creates a dynamic list. Here we make a list of reversed tuples and sorted it.
# (v,k) for k,v in list - (v,k) is like a stamp, each time the code runs the line it will stamp that request (v,k)
c = {'a':10,'b':1,'c':22}
print(sorted([(v,k) for k,v in c.items()]))

# TUPLES and COMPOSITE KEYS in dictionaries
# Use a tuple as the key (it will have inside two keys)
directory[last,first] = number    #expression [last,first] is a tuple
for last,first in directory:
    print(first,last,directory[last,first])

# Tuples dont provide methods like sort and reverse because they are immutable.
# However, Python provides the built-in functions sorted and reversed.
# This functions take any sequence as a parameter and return a new sequence.
