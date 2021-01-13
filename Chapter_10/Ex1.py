# Exercise 1: Revise a previous program as follows: Read and parse the
# “From” lines and pull out the addresses from the line. Count the num-
# ber of messages from each person using a dictionary.
# After all the data has been read, print the person with the most commits
# by creating a list of (count, email) tuples from the dictionary. Then
# sort the list in reverse order and print out the person who has the most
# commits.


# Option 1
fname = input('Enter file name:')
if len(fname) < 1 : fname = "mbox-short.txt"
fhandle = open(fname)
emails = {}
for line in fhandle:
    if line.startswith('From '):
        line = line.rstrip()
        words = line.split()
        emails[words[1]] = emails.get(words[1],0) +1
print(emails)
lst = list()
for k,v in emails.items():
    lst.append((v,k))
lst = sorted(lst, reverse=True)
print(lst[:1])

# Option 2
fname = input('Enter file name:')
if len(fname) < 1 : fname = "mbox-short.txt"
fhandle = open(fname)
emails = {}
for line in fhandle:
    if line.startswith('From '):
        line = line.rstrip()
        words = line.split()
        emails[words[1]] = emails.get(words[1],0) +1
print(emails)
lst = list()
for k,v in emails.items():
    newtup = (v,k)
    lst.append(newtup)
lst = sorted(lst,reverse=True)
for v,k in lst[:1]:
    print(k,v)