# Exercise 4: Add code to the above program to figure out who has the
# most messages in the file. After all the data has been read and the dic-
# tionary has been created, look through the dictionary using a maximum
# loop (see Chapter 5: Maximum and minimum loops) to find who has
# the most messages and print how many messages the person has.

fname = input('Enter file name:')
if len(fname) < 1 : fname = "mbox-short.txt"
fhandle = open(fname)
emails = {}
bigemail = None
bigcount = None
for line in fhandle:
    if line.startswith('From '):
        line = line.rstrip()
        words = line.split()
        emails[words[1]] = emails.get(words[1],0) +1
for mails,count in emails.items():
    if bigemail is None or count > bigcount:
        bigemail = mails
        bigcount = count
print(emails)
print(bigemail,bigcount)
