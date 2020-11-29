
sum=0
count=0
while True:
    try:
        snumber=input ("Enter a number: ")
        if snumber == "done":
            break
        else:
            inumber=int(snumber)
            sum=sum+inumber
            count=count+1
    except:
        print("Invalid Input")
print(sum," ",count," ",sum/count)