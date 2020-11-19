#Ex.1/2 Employee payment. (overtime >40 pay 1.5)  (Rate: 10)

shours = input("Enter Hours\n")
srate = input("Enter rate\n")
try:
    hours = float(shours)
    rate = float(srate)
    if hours > 40:
        reg = hours * rate
        extra = (hours - 40) * (rate * 0.5)
        pay = reg + extra
        print(pay)
    else:
        pay = hours * rate
        print(pay)
except:
    print("Error, please enter numeric input")