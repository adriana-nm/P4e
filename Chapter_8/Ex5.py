# Request a file & extract the email of the "From" lines.
# Create a count of the emails. Print it at the end.

fname = input('Introduce the name of the file:')
fhandle = open(fname)
count = 0
for line in fhandle:
    if line.startswith('From '):
        line = line.split()
        print(line[1])
        count = count + 1
print('There were',count,'lines in the file with From as the first word')