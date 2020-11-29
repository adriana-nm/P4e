#While: For indefinite loops
#For: For definite loops

#While Iteration
n=5
while n>0:
    print(n)
    n=n-1
print("End")


#Infinite Loop + Break (Break: Gets out of the loop)
while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done!')


#Finite Iterations: While + continue (Continue: Doesnt run the next code, but go back to the start of the loop)
while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')

#Basic For pattern
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year:', friend)
print('Done!')

#Count with a loop
#(Not very useful, you can use the function len() )
count = 0
for itervar in [3, 41, 12, 9, 74, 15]:
    count = count + 1
print('Count: ', count)

x=(3, 41, 12, 9, 74, 15)
print(len(x))

#Sum with a loop
#(Not very useful, you can use the function sum() )
total=0
for itervar in [3, 41, 12, 9, 74, 15]:
    total = total + itervar
print("Total:", total)

x=(3, 41, 12, 9, 74, 15)
print(sum(x))

#Average with a loop
#(Not very useful, you can use the function statistic.mean() )
#1
sum=0
count=0
for numbers in (10, 20, 100):
    sum=sum+numbers
    count=count+1
print(sum/count)

#2 with built-in function
import statistics
print(statistics.mean ([10, 20, 100]))


#Search of a value, with a boolean (True or False) variable (to know if a value was found in a list)

found = False
for values in (4, 6, 3, 8, 7, 5):
    if values == 8:
        found = True
        break
print(found)


#Maximum with a loop (with no built-in function Max() )

largest = None
print('Before:', largest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if largest is None or itervar > largest :
        largest = itervar
    print('Loop:', itervar, largest)
print('Largest:', largest)

#None: Representation of not having a data. Is a type variable. Equals to absence of a value.



#Minimum with a loop (with no built-in function Min ())

smallest = None
print('Before:', smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest :
        smallest = itervar
    print('Loop:', itervar, smallest)
print('Smallest:', smallest)

#Minimum with a loop (with a created function, called Mini)

def mini(values):
    smallest = None
    for value in values:
        if smallest is None or value < smallest:
            smallest = value
    print(smallest)
    return smallest

mini ([5,30,4])

#Introduce a list of values in a function must be inside []
#But if you introduce a list of values inside a variable, theres no need of [], you just use ()



#Minimum with python Min function // Same with max()

#1
print(min([55,40,25,70,60,3]))

#2
a=(5,3,6,1)
print(min(a))

#3
print(min(["Pedro","Ana","Jorge"]))


#is / is not operators
#Used in logical expressions. Implies "is the same as". Similar but stronger thatn ==
#Usually you use it for a true, false or none
