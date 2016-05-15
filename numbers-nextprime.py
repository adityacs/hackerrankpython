#Next Prime Number 
#Have the program find prime numbers 
#until the user chooses to stop asking for the next one

def next_prime():
	global num
	while True:
		num = num + 1
		if num == 2:
			return num
		for i in range(2, num):
			if num % i == 0:
				break
		else:
			break
	return num


def main():
	global num
	num = 1
	while True:
		user_input = raw_input("Enter yes to continue or q to quit")
		if user_input == 'yes':
			print next_prime()
		else:
			break	


if __name__ == '__main__':
	main()