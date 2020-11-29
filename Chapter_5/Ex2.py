max = None
min = None
while True:
    try:
        snumber=input ("Enter a number: ")
        if snumber == "done":
            break
        else:
            inumber=int(snumber)
            if max is None or inumber > max:
                max=inumber
            if min is None or inumber < min:
                min=inumber
    except:
        print("Invalid Input")
print(max," ",min)