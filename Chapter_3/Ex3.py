# Ex.3
sscore = input("Enter a score\n")
try:
    score = float(sscore)
    if score <= 0.0 or score >= 1.0:
        print("Bad score")
    elif score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score >= 0.6:
        print("D")
    elif score < 0.6:
        print("F")
except:
    print("NOT NUMBER")
