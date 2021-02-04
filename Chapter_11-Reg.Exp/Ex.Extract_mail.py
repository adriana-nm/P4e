# Different ways to extract a host address of an email in the different parts of the book

data = 'From stephen.marquard@utc.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
sppos = data.find(' ',atpos)
host = data[atpos+1:sppos]
print(host)

line = 'From stephen.marquard@utc.ac.za Sat Jan 5 09:14:16 2008'
words = line.split()
email = words[1]
parts = email.split('@')
print(parts[1])

import re
line = 'From stephen.marquard@utc.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('@(\S+)',line)
print(y)

import re
line = 'From stephen.marquard@utc.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('@([^ ]*)',line)
print(y)
