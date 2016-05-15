# Enter your code here. Read input from STDIN. Print output to STDOUT
"""
string = raw_input()
string1 = ""
for s in string:
    if s.isupper():
        string1 = string1 + s.lower()
    elif s.islower():
        string1 = string1 + s.upper()
    else:
    	string1 = string1 + s
print string1        
"""

"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
string = raw_input()
string1 = ""
print string.split(' ')
for s in string.split(' '):
	if not s.isspace() and len(s) > 1:
		if s[0].isupper() or s[0].islower():
			string1 = string1 + s[0].upper()
		elif s[0].isalpha() or s[0].isdigit():
			string1 = string1 + s[0]
		string1 = string1 + s[1:]
	else:
		string1 = string1 + s.upper()
	string1 = string1 + " "
print string1        
"""
