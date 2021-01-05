# Exercise 3: Encapsulate this code in a function named count, and
# generalize it so that it accepts the string and the letter as arguments.

def contarletra():
    word= input("Enter the word: ")
    letter = input("Enter the letter: ")
    count=0
    for letters in word:
        if letters == letter:
            count=count+1
    print(count)

contarletra()