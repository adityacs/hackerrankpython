#'{1}{0}{1}'.format(s.join(lis), s)

import string
alphabet = list(string.ascii_lowercase)
n = int(raw_input())
alphabet1 = [alphabet[x] for x in range(n)]
alphabet2 = list(reversed(alphabet1))
string1 = "".join(alphabet1)
string2 = "".join(alphabet2)
num = ((n-1)*4)+1
count = 0
for i in range(1, (n+1)):
	x = 1 * i
	y = -1 * i
	if y+1 == 0:
		string = "-" * (((num-len(string2[:x])) / 2) - count) + string2[:x] + "-" * (((num-len(string2[:x])) / 2) - count)
	else:
		a = string2[:x]
		b = string1[y+1:]
		string = "-" * (((num-len(a+b)) / 2) - count)  + "-".join(a) + "-" +"-".join(b) + "-" * (((num-len(a+b)) / 2) - count)
	print string
	count+=1
count = (n-2)
for i in range((n-1), 0, -1):
	x = 1 * i
	y = -1 * i
	if y+1 == 0:
		string = "-" * (((num-len(string2[:x])) / 2) - count) + string2[:x] + "-" * (((num-len(string2[:x])) / 2) - count)
	else:
		a = string2[:x]
		b = string1[y+1:]
		string = "-" * (((num-len(a+b)) / 2) - count) + "-".join(a) + "-" + "-".join(b) + "-" * (((num-len(a+b)) / 2) - count)
	print string
	count-=1