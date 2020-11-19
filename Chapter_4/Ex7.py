# Ex.3
def nota(score):
    if score <= 0.0 or score >= 1.0:
        return "Bad score"
    elif score >= 0.9:
        return "A"
    elif score >= 0.8:
        return "B"
    elif score >= 0.7:
        return "C"
    elif score >= 0.6:
        return "D"
    elif score < 0.6:
        return "F"

print(nota(0.95))

