# Exercise 3: Write a program that reads a file and prints the letters
# in decreasing order of frequency. Your program should convert all the
# input to lower case and only count the letters a-z. Your program should
# not count spaces, digits, punctuation, or anything other than the letters
# a-z. Find text samples from several different languages and see how
# letter frequency varies between languages. Compare your results with
# the tables at https://wikipedia.org/wiki/Letter_frequencies.

import string
fname = input('Introduce the file name:')
if len(fname) < 1: fname = r'C:\Users\adri_\PycharmProjects\P4E\Chapter_9\romeo.txt'
fhandle = open (fname)
abc = {}
templist = list()
for line in fhandle:
    line = line.rstrip()
    line = line.translate(line.maketrans('','',string.punctuation + string.digits))
    line = line.lower()
    words = line.split()
    for word in words:
        letters = list(word)
        for letter in letters:
            abc[letter] = abc.get(letter,0) + 1
for k,v in abc.items():
    newtpl = (v,k)
    templist.append(newtpl)
templist.sort(reverse=True)
print(templist)
