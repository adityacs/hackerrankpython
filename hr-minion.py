string = raw_input()
vowels = ['A', 'E', 'I', 'O', 'U']
stuart_list = []
kevin_list = []
staurt_score = 0
kevin_score = 0
for i in range(len(string)):
	if string[i] in vowels:
		for j in range(i, len(string)):
			if string[i:j+1] not in kevin_list:
				kevin_list.append(string[i:j+1])
				kevin_score+=1
			else:
				kevin_score+=1
	else:
		for j in range(i, len(string)):
			if string[i:j+1] not in stuart_list:
				stuart_list.append(string[i:j+1])
				staurt_score+=1
			else:
				staurt_score+=1
if kevin_score > staurt_score:
	print "Kevin", kevin_score
elif kevin_score < staurt_score:
	print "Stuart", staurt_score
else:
	print Draw

"""
code from hackerrank
s = raw_input()

vowels = 'AEIOU'

kevsc = 0
stusc = 0
for i in range(len(s)):
    if s[i] in vowels:
        kevsc += (len(s)-i)
    else:
        stusc += (len(s)-i)

if kevsc > stusc:
    print "Kevin", kevsc
elif kevsc < stusc:
    print "Stuart", stusc
else:
    print "Draw"