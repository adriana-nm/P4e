# A KEY is the reference of a VALUE

# CREATE a dictionary (dict function)
eng2sp = dict()
print(eng2sp)

# ADD data to the dictionary already created
# Key = 'one', value = 'uno'. The pair is called key-value pair or an item.
eng2sp['one'] = 'uno'
print(eng2sp)

# CREATE a dictionary WITH DATA INCLUDED
eng2sp = {'one':'uno','two':'dos','three':'tres'}
print(eng2sp)

# REPLACE a value of a Key.
eng2sp['three'] = 'tercero'
print(eng2sp)

# SEARCH/LOOK UP for a value (use a Key)
# If the key is not in the dictionary, you get an error.
print(eng2sp['two'])

# LEN function, returns the number of key-value pairs.
print(len(eng2sp))

# IN OPERATOR. It tells if something appear as A KEY in the dictionary (not as a value)
# Boolean. Returns True/False.
'one' in eng2sp
'uno' in eng2sp

# FIND A VALUE. First you need to use the method VALUES to return data than can be converted into a list.
# Then you con use the in operator to search for the value you need.
eng2sp = {'one':'uno','two':'dos','three':'tres'}
vals = list(eng2sp.values())
print('uno' in vals)            # Return True/False

# Print keys, values, and items
names = {'chuck':1,'annie':42,'jan':100}
print(list(names))      # Return keys
print(names.keys())     # Return dict_keys(list of keys)
print(names.values())   # Return dict_values(list of values)
print(names.items())    # Return dict_items (with the keys and its corresponding values)

names = {'chuck':1,'annie':42,'jan':100}  #Returns keys and its values
for aaa,bbb in names.items():
    print(aaa,bbb)

# DICTIONARY AS A SET OF COUNTERS

# Ex. Count how many times appears each letter in a word
word = 'brontosaurus'
d = dict()
for c in word:
    if c not in d:
        d[c] = 1
    else:
        d[c] = d[c] + 1
print(d)

# Ex. Same exercises but using the method GET.
# GET - Takes a key and a default value. If key appears returns the value, if not returns the default value (that I put there).
word = 'brontosaurus'
d = dict()
for c in word:
    d[c] = d.get(c,0) + 1
print(d)

# DICTIONARIES AND FILES

# Alternatives to increment a variable
# count[word] = count[word] + 1
count[word] +=1
# It work with +=, -=, *=, /=

# Ex. Read a file and count how many words (text with no punctuation)
# You can also use the method GET.
fname = input('Enter the file name:')
try:
    fhandle = open(fname)
except:
    print('File',fname,'cannot be opened')
    exit()
counts = dict()
for line in fhandle:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
print(counts)

#LOOPING IN DICTIONARIES

# Ex. print each key with it's corresponding value
counts = {'chuck':1,'annie':42,'jan':100}
for key in counts:
    print(key,counts[key])

# Ex. Find all entries with a condition. Example with a value >10.
counts = {'chuck':1,'annie':42,'jan':100}
for key in counts:
    if counts[key] > 10:
        print(key,counts[key])

# Ex. Sort the keys and print it
# First make a list (using KEY METHOD), then sort the list, then print the list (key+values)
counts = {'chuck':1,'annie':42,'jan':100}
lst = list(counts.keys())
lst.sort()
for key in lst:
    print(key,counts[key])

# Ex. Find the key word that appears the most in a text
# If there are 2 words that appear the same amount of time, it will show only 1.
fname = input('Enter file name:')
fhandle = open(fname)
counts = dict()
for line in fhandle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1
bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)

# TEXT PARSING

# str.translate(str.maketrans (from, to, delete)). Replace characters in from with characters in the same position in to. Also delete characters in delete.
# str.translate requires a translation table. Maketrans provides the translation table.

str.maketrans()

# Ex. Read a file and count how many words. Text with punctuation.
# Beware of: capital letters, punctuation
# Punctuation: We request Python to inform characters that are punctuation and we put them in the delete section of str.maketrans()
import string
fname = input('Enter the file name:')
try:
    fhandle = open(fname)
except:
    print('File cannot be opened:',fname)
    exit()
counts = dict()
for line in fhandle:
    line = line.rstrip()
    line = line.translate(line.maketrans('','',string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
print(counts)