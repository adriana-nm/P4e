#Print:
# *****
# ****
# ***
# **
# *


a="*"
n=5
for i in range(n):
    print(a*n)
    n=n-1


n=5
for i in range(n):
    print(("*****")[0:n])
    n=n-1


n=5
x=5
while n>0:
    while x>0:
        print("*", end="")
        x=x-1
    n=n-1
    x=n
    print("")


for x in range(5,0,-1):
    for n in range(x):
        print("*", end="")
    print("")


for x in range(5):
    for y in range(5-x):
        print("*", end="")
    print("")


def solucion5(n):
    for x in range(n):
        for y in range(n-x):
            print("*", end="")
        print("")

solucion5(8)