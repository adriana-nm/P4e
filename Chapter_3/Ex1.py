#Ex.1/2 Employee payment. (overtime >40 pay 1.5)  (Rate: 10)
shours = input("Enter Hours\n")
srate = input("Enter rate\n")
try:
    hours = float(shours)
    rate = float(srate)
    if hours>40:
        pay = (40*rate)+((hours-40)*(rate*1.5))
    else:
        pay = hours*rate
    print(pay)
except:
    print("Error, please enter numeric input")