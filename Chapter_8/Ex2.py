# Create a file with text that might cause the program to fail.
# Possibilities: Numbers, signs, less words than the amount I requested.
# Fix it.

fhandle = open('testlist.txt','w')
line1 = '123 34 456\n'
line2 = 'letras\n'
line3 = '\n'
line4 = '+- letras --*\n'
line5 = 'more music please'
fhandle.write(line1)
fhandle.write(line2)
fhandle.write(line3)
fhandle.write(line4)
fhandle.write(line5)
fhandle.close()

fhand = open('testlist.txt')
n = 2
for line in fhand:
    # print('debug:',line)
    words = line.split()
    # print('debug:', line)
    if len(words) == 0:
        continue
    if words[0] == 'From':
        continue
    if len(words) > n:
        print(words[n])
    else:
        print(words[-1])
