#Solution 1
text = "X-DSPAM-Confidence:    0.8475"
colpos = text.find(":")
text2 = text[colpos+1:]
text3 = text2.lstrip()
flnumber = float(text3)
print(flnumber)

#Solution 2
text = "X-DSPAM-Confidence:    0.8475"
colpos = text.find(":")
text2 = text[colpos+1:]
number = float (text2)
print(number)