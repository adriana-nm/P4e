# Exercise 2: Write a program that categorizes each mail message by
# which day of the week the commit was done. To do this look for lines
# that start with “From”, then look for the third word and keep a running
# count of each of the days of the week. At the end of the program print
# out the contents of your dictionary (order does not matter).
# Sample Line:
# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

fname = input('Enter the file name:')
fhandle = open(fname)
days = {}
for line in fhandle:
    line = line.rstrip()
    if line.startswith('From '):
        words = line.split()
        days[words[2]] = days.get(words[2],0) +1
print(days)