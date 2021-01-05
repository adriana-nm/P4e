# Prompts the user to enter a list of integer numbers until the user write 'done'
# Store the numbers in a list, and use the max/min functions and print it.

nlist = []
while True:
    snumb = input('Type a number:')
    if snumb == 'done':
        break
    try:
        inumb = int(snumb)
    except:
        continue
    nlist.append(inumb)
print('Maximum:',max(nlist))
print('Minimum:',min(nlist))