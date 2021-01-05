# OPEN A FILE

#def open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None,
#    'r'       open for reading (default)
#    'w'       open for writing, truncating the file first
#    'x'       create a new file and open it for writing
#    'a'       open for writing, appending to the end of the file if it exists
#    'b'       binary mode
#    't'       text mode (default)
#    '+'       open a disk file for updating (reading and writing)

# file.open()
# file.write()
# file.close()

#READING FILES

# Read all the text inside the file
fhand = open('../mbox-short.txt')
print(fhand.read())

# Read the first line of the text. If I repeat it below, I read the second and so on.
fhand = open('../mbox-short.txt')
print(fhand.readline(5))

# Returning amount of lines a file has (Very fast for big files)
# If the file is too big for main memory, nee to read it in chunks, using for or while loop
# "../" Because the file is not in this folder, its outside this folder.
# A file read using a loop, will be split into lines using newline character (/n)
fhand = open('../mbox-short.txt')
count = 0
for line in fhand:
    count = count + 1
print('Line count: ',count)

# Return amount of characthers a file has (Use for small files, or it will require a lot of memory)
fhand = open ('../mbox-short.txt')
inp = fhand.read()
print(len(inp))

# Good practice - Store output of read as a variable, because each call to read exhaust the resource.
# Example: Second print will result in zero
fhand = open ('../mbox-short.txt')
print(len(fhand.read()))
print(len(fhand.read()))

# Very common to read a file  processing only the ones with a condition
# Select only the lines with the prefix "From"
fhand = open('../mbox-short.txt')
count = 0
for line in fhand:
    if line.startswith('From:'):
        print(line)

# Use rstrip to delete the whitespace after each line of information (previous exercise)
fhand = open ('../mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)

# Use find to search information in the text and print those lines
fhand = open('../mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.find('@uct.ac.za') == -1: continue
    print(line)

# Allow the user to enter the filename, to use different files
fname = input('Enter the file name:')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were',count,'subjects lines in',fname)

# Allow the user to enter a filename but protecting the code from wrong names of files
# QUIT AND EXIT are the same. They exit the program.
fname = input('Enter the file name:')
try:
    fhand = open(fname)
except:
    print('File',fname,'cannot be opened')
    exit()
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were',count,'subjects lines in',fname)

# Write a File. Open with mode 'w'. // IT CREATE A FILE!
# If the file already exist, this mode clears out the old data and start fresh
# If the file doesnt exist, a new one is created.

fout = open ('output.txt','w')
print(fout)

# Introduce data into the new file. If I print it, it will return the number of characthers written.
# We need to end it with \n to mark the new line. Otherwise we'll replace it the next time we introduce a text.
line1 = "This here's the wattle,\n"
fout.write(line1)

# FLUSH - If we want to save the data on the disk, but still dont close the file
fout.flush()

# We need to close the file, to make sure all the data is physically written to the disk (it wont be lost if power goes off).
line2 = 'the emblem of our land.\n'
fout.write(line2)
fout.close()

# Read the new file created.
text = open('output.txt')
for line in text:
    line = line.rstrip()
    print(line)

# Repr function to see blank spaces and lines.
s = '1 2\t 3\n 4'
print (s)
print(repr(s))