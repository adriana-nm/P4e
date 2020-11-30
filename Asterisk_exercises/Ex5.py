#Pattern 5:
#    *
#   ***
#  *****
# *******

def star5(n):
    x=1
    y=(n-1)
    for rows in range(n):
        for blank in range(y):
            print(" ", end="")
        for dots in range(rows+x):
            print("*", end="")
        x=x+1
        y=y-1
        print("")

star5(8)

#Pattern 6:
# *******
#  *****
#   ***
#    *

def star6(n):
    x=n-1
    y=n
    for rows in range(n):
        for blank in range(rows):
            print(" ", end="")
        for dots in range(y+x,0,-1):
            print("*", end="")
        x=x-1
        y=y-1
        print("")

star6(5)

#Pattern 7: (only odd numbers)

#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *

def star7(n):
    sw = ((n - 1) / 2)
    w = int(sw)
    x = 1
    for rows in range (n):
        for blank in range(w):
            print(" ", end="")
        for dots in range (x):
            print("*", end="")
        if rows < (n-1)/2:
            w=w-1
            x=x+2
        else:
            w=w+1
            x=x-2
        print("")

star7(5)


#Pattern 7 using a FLAG.

def star7b(n):
    sw = ((n - 1) / 2)
    w = int(sw)
    x = 1
    flag = True
    for rows in range (n):
        for blank in range(w):
            print(" ", end="")
        for dots in range (x):
            print("*", end="")
        if flag:
            w=w-1
            x=x+2
            flag = rows+1 < (n - 1) / 2
        else:
            w=w+1
            x=x-2
        print("")

star7b(7)



#Pattern 8: (only odd numbers)
# *
# **
# ***
# ****
# ***
# **
# *

def star8(n):
    x=1
    for rows in range(n):
        for dots in range(x):
            print("*", end="")
        print("")
        if rows < ((n-1)/2):
            x=x+1
        else:
            x=x-1

star8(7)


#Pattern 9:
#    *
#   **
#  ***
# ****
#  ***
#   **
#    *

def star9(n):
    x=1
    sy=(n-1)/2
    y=int(sy)
    for rows in range(n):
        for blank in range(y):
            print(" ", end="")
        for dots in range(x):
            print("*", end="")
        print("")
        if rows < ((n-1)/2):
            x=x+1
            y=y-1
        else:
            x=x-1
            y=y+1

star9(7)


#Pattern 10:
#     *****
#    *****
#   *****
#  *****
# *****

def star10(n):
    x=n-1
    for rows in range(n):
        for blank in range(x):
            print(" ", end="")
        for dots in range(n):
            print("*", end="")
        print("")
        x=x-1

star10(5)

#Pattern 11:
#     *****
#    *****
#   *****
#  *****
# *****

def star11(n):
    for rows in range(n):
        for blank in range(rows):
            print(" ", end="")
        for dots in range(n):
            print("*", end="")
        print("")


star11(5)

#Pattern 12:
# *****
# ****
# ***
# **
# *
# **
# ***
# ****
# *****

def star12(n):
    sx=(n+1)/2
    x=int(sx)
    for rows in range(n):
        for dots in range(x):
            print("*", end="")
        print("")
        if rows < (n-1)/2:
            x=x-1
        else:
            x=x+1

star12(9)


#Pattern 13:
# *****
#  ****
#   ***
#    **
#     *
#    **
#   ***
#  ****
# *****

def star13(n):
    sx=(n+1)/2
    x=int(sx)
    y=0
    for rows in range(n):
        for blank in range(y):
            print(" ", end="")
        for dots in range(x):
            print("*", end="")
        print("")
        if rows < (n-1)/2:
            x=x-1
            y=y+1
        else:
            x=x+1
            y=y-1

star13(9)