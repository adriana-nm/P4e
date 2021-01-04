#Ex. Request a file, read it and transform all in upper case.

name = input('Enter a file name:')
text = open(name)
for line in text:
    line = line.rstrip()
    line = line.upper()
    print(line)