# Fibonacci Sequence Generator
# Have the user enter a number and
# generate a fibonacci sequence
# which size is equivalent to that number.

def fibonacci(n):
	
	assert n > 0

	list = [1]

	while len(list) < n:
		if len(list) == 1:
			list.append(1)
		else:	
			list.append(list[-1]+list[-2])

	#convert numbers to string		
	for i in range(len(list)):
		list[i] = str(list[i])	

	return(', '.join(list))  # Return the sequence seperated by commas		
	

def main():
	print(fibonacci(int(raw_input("Enter a number: "))))

if __name__ == '__main__':
	main()

	