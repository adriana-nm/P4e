# Exercise 3: Write a program to read through a mail log, build a his-
# togram using a dictionary to count how many messages have come from
# each email address, and print the dictionary.

fname = input('Enter file name:')
fhandle = open(fname)
emails = {}
for line in fhandle:
    if line.startswith('From '):
        line = line.rstrip()
        words = line.split()
        emails[words[1]] = emails.get(words[1],0) +1
print(emails)
