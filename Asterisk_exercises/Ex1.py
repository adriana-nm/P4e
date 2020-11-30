#https://www.javainterviewpoint.com/star-pattern-programs-in-java/
#Beware: Range start in zero, and it goes till n-1 (is not inclusive)

#Pattern 1
# *
# **
# ***
# ****
# *****

def star1(n):
    for rows in range(n):
        for dots in range(rows+1):
            print("*", end="")
        print("")

star1(5)

#Pattern 2
#     *
#    **
#   ***
#  ****
# *****

def star2(n):
    for rows in range(n):
        for blank in range(n-rows-1,0,-1):
            print(" ", end="")
        for dots in range (rows+1):
            print("*", end="")
        print()

star2(5)

#Pattern 3
# *****
# ****
# ***
# **
# *

def star3(n):
    for rows in range(n):
        for dots in range(n - rows):
            print("*", end="")
        print("")

star3(5)

#Pattern 4
# *****
#  ****
#   ***
#    **
#     *

def star4(n):
    for rows in range (n):
        for blank in range (rows):
            print(" ", end="")
        for dots in range (n-rows):
            print("*", end="")
        print("")

star4(5)