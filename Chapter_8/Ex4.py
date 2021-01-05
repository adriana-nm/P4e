# Open the file, read it. Split the line into a list of words.
# Search if the words below are on the list or not.
# If they are not, add it to the list. Sort it and print it in alphabetical order.

wordlist = ['Arise', 'But', 'It', 'Juliet', 'Who', 'already',
'and', 'breaks', 'east', 'envious', 'fair', 'grief',
'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft',
'sun', 'the', 'through', 'what', 'window',
'with', 'yonder']

fhand = open('romeo.txt')
nlist = []
for line in fhand:
    nwords = line.split()
    nlist.extend(nwords)
for word in wordlist:
    try:
        nlist.index(word)
    except:
        nlist.append(word)
nlist.sort()
print(nlist)