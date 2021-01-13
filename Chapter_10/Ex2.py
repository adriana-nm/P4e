# Exercise 2: This program counts the distribution of the hour of the day
# for each of the messages. You can pull the hour from the “From” line
# by finding the time string and then splitting that string into parts using
# the colon character. Once you have accumulated the counts for each
# hour, print out the counts, one per line, sorted by hour.

fname = input('Introduce the file name:')
if len(fname) < 1: fname = 'mbox-short.txt'
fhandle = open (fname)
histogram = {}
for line in fhandle:
    if line.startswith('From '):
        line = line.rstrip()
        line = line.split()
        time = line[5]
        hour = time[0:2]
        histogram[hour] = histogram.get(hour,0) + 1
print(histogram)
for k,v in sorted(histogram.items()):
    print(k,v)