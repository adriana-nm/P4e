# Ex. Request a file, read it and search the text X-DSPAM-Confidence.
# Count the lines and sum each confidence, at last obtain the average spam confidence.

fname = input ('Enter the file name:')
count = 0
tsum = 0
text = open(fname)
for line in text:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence'):
        pointpos = line.find(':')
        snum = line[pointpos+1:]
        num = float(snum)
        count = count + 1
        tsum = tsum + num
print(tsum/count)
