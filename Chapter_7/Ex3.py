# Ex. Put an Easter Egg in the program, if you write "booo"

fname = input('Enter the file name:')
if fname == "booo":
    print("Boo to you - You have been punk'd")
    exit()
text = open(fname)
count = 0
for line in text:
        count = count + 1
print("There were",count,"subject lines in",fname)