# Matches:
# abc…	Letters
# 123…	Digits
# \d	Any Digit
# \D	Any Non-digit character
# .	    Any Character
# \.	Period
# [abc]	 Only a, b, or c (Matches a single character in the listed set)
# [^abc] Not a, b, nor c (Matches a single character not in the listed set)
# [a-z]	 Characters a to z (The set of characters can include a range)
# [0-9]	 Numbers 0 to 9
# \w     Any Alphanumeric character
# \W     Any Non-Alphanumeric character
# {m}    m Repetitions   (Ex. a{2})
# {m,n}  m to n Repetitions  (From m to n repetitions)
# \s     Any whitespace
# \S     Any non whitespace character
# ^  Matches the beginning of a line
# $  Matches the end       of a line (Ex. successful$)
# *  Repeats a character zero or more times (Greedy: It match the largest possible string)
# *? Repeats a character zero or more times (non-greedy) (it matches the shortest string)
# +  Repeats a character one or more times
# +? Repeats a character one or more times (non-greedy)
# (       Indicates where the string extraction is to start
# )       Indicates where the string extraction is to end
# ?	 Optional character (it will match if the character is or not, ex Files?, will match File and Files.
# (a(bc))	Capture Sub-group
# (abc|def)	Matches abc or def
# \b        Matches the boundary between a word and a non-word character (Ex. What the $%&%!)

#import re
#re.search() To see if a string matches a reg. exp.
#re.findall() Extract a portion of a string that match the reg. exp.

# Find the text 'From:' in the line:
import re
hand=open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.searh('From:',line):
        print(line)

# Find if it starts with the text 'From':
import re
hand=open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.searh('^From:',line):
        print(line)

# Pattern: To find something that starts with X has characters and end with semicolon
^X.*: (^start with X, then . match any character, * many times)

# Pattern: to find something that starts with X- and follow characters without spaces, and end with semicolon
^X-\S+:

# Extract all the digits in the text
import re
x= 'My 2 favorite numbers are 19 and 36':
y= re.findall('[0-9]+',x)
print(y)

# Extract all the vocals as upper letters
import re
x= 'My 2 favorite numbers are 19 and 36'
y= re.findall('[AEIOU]+',x)
print(y)

# Non-Greedy matching: ^F.+?:  (Result: 'From:')
import re
x = 'From: Using the : character'
y = re.findall('^F.+?:',x)
print(y)

# Greedy matching: ^F.+:  (Result: 'From: using the :')
import re
x = 'From: Using the : character'
y = re.findall('^F.+:',x)
print(y)

# Extract and email
import re
x = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('\S+@\S+',x)
print(y)

# Extract and email, only if the line starts with From
import re
x = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('^From (\S+@\S+)',x)
print(y)

# Match non-blanck characters: [^ ]*
import re
x = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('^From .*@([^ ]*)',x)
print(y)

#Escape Character: If you want a reg. exp. character behave normal you add \ before the character.
import re
x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+',x)
print(y)

# Ex. Search the DSPAM confidence, add it to a list and find the maximum number.
import re
hand = open('mbox-short.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    snum = re.findall('^X-DSPAM-Confidence: ([0-9.]+)',line)
    if len(snum) != 1: continue
    fnum = float(snum[0])
    numlist.append(fnum)
print('Maximum:',max(numlist))

# m repetitions
import re
x = 'We just received $10.00 for cookies'
y = re.findall('.o{2}.+',x)
print(y)

# Subgroups
import re
years = 'Jan 1987, May 1969, Aug 2011'
y = re.findall('(\S+ (\d+))', years)
print(y)

# Logic
import re
regex = r'(I love (cats?|dogs?)),'
text ='I love cats, I love dogs, I love logs, I love cogs'
y = re.findall(regex, text)
print('%s' % (y))

# Match a string and print groups
import re
regex = r'([a-zA-Z]+) (\d+)'
if re.search(regex, "June 24"):
    match = re.search(regex, 'June 24')
    print('Match at index %s, %s' % (match.start(), match.end()))
    print('Full match: %s' % (match.group(0)))
    print('Month: %s' % (match.group(1)))
    print('Day: %s' % (match.group(2)))
else:
    print("The regex pattern does not match")

# Find and print all the dates in the string
import re
regex = r'[a-zA-Z]+ \d+'
matches = re.findall(regex, 'June 24, August 9, December 12')
for match in matches:
    print("Full match: %s" % (match))

# Find and print all the months in the string
import re
regex = r'([a-zA-Z]+) \d+'
matches = re.findall(regex, 'June 24, August 9, December 12')
for match in matches:
    print("Match month: %s" % (match))

# Find and replace strings (with re.sub )
import re
regex = r'([a-zA-Z]+) (\d+)'
print(re.sub(regex,r'\2 of \1', 'June 24, August 9, December 12'))

# Compile a pattern. It will no longer demand you enter the patterm into each method
import re
regex = re.compile(r'(\w+) World')
result = regex.search("Hello World iS easy")
if result:
    print(result)                                          #Will print the object, span, matched string
for result in regex.findall("Hello World, Bonjour World"):
    print(result)                                          #Will print Hello, Bonjour
print(regex.sub(r'\1 Earth', "Hello World"))               #Will print Hello Earth (we change World for Earth)
