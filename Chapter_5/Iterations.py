#Infinite Loop + Break
while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done!')



#Finite Iterations: While + continue
while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')

