# Exercise 5: This program records the domain name (instead of the
# address) where the message was sent from instead of who the mail came
# from (i.e., the whole email address). At the end of the program, print
# out the contents of your dictionary.

fname = input('Enter file name:')
if len(fname) < 1 : fname = "mbox-short.txt"
fhandle = open(fname)
domains = {}
for line in fhandle:
    line = line.rstrip()
    if line.startswith('From '):
        atpos = line.find('@')
        spapos = line.find(' ',atpos)
        domains[line[atpos+1:spapos]] = domains.get(line[atpos+1:spapos],0) +1
print(domains)