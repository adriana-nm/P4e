#Print:
# *******
#  *****
#   ***
#    *

x=7
for i in range(4):
    print((" "* i), end="")
    for j in range(x):
        print("*", end="")
    x=x-2
    print("")

i=0
for x in range(7,0,-2):
    print((" "* i), end="")
    for n in range(x):
        print("*", end="")
    i=i+1
    print("")

def solucionC(n):
    i=0
    for x in range(n,0,-2):
        print((" "* i), end="")
        for n in range(x):
            print("*", end="")
        i=i+1
        print("")

solucionC(9)