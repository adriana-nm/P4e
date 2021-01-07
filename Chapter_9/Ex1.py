# Write a program that reads the words in words.txt and stores them as
# keys in a dictionary. It doesn’t matter what the values are. Then you
# can use the in operator as a fast way to check whether a string is in the
# dictionary.

fname = input('Enter the file name:')
fhandle = open(fname)
textwords = dict()
for line in fhandle:
    words = line.split()
    for word in words:
        textwords[word] = textwords.get(word,0)
string = input('Enter a word:')
if string in textwords:
    print('The word: "',string,'" is in the text')
else:
    print('The word: "',string,'" is not in the text')
