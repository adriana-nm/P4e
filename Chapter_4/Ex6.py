#Ex. Employee payment. (overtime >40 pay 1.5) Use a Function!

def computepay(hours, rate):
    if hours > 40:
        reg = hours * rate
        extra = (hours - 40) * (rate * 0.5)
        pay = reg + extra
    else:
        pay = hours * rate
    return pay

print(computepay(45,10))
