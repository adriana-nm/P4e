# Rewrite Ex.2 without the two if statements.
# Use a compound logical expression ussing the or logical operator with a single if statement.

fhand = open('testlist.txt')
n = 2
for line in fhand:
    words = line.split()
    if len(words) == 0 or len(words) <= n:
        continue
    else:
        print(words[n])
