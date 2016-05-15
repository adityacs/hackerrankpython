#Factorial Finder
#The factorial of a positive integer n 
#is defined as the product of the sequence
#n-1, n-2, ...1 and the factorial of 0 is 
#defined as being 1
#Solve this using both loops and recursion


#recursion
"""
def factorial(n):
	if n < 2:
		return 1
	else:
		return n * factorial(n-1)	

def main():
	print(factorial(int(raw_input("Enter a number: "))))

if __name__ == '__main__':
	main()
"""

#loop

def factorial(n):
	if n < 2:
		return 1
	else:
		fact = 1
		for i in range(2, n+1):
			fact = fact * i
		return fact
		
def main():
	print(factorial(int(raw_input("Enter a number: "))))

if __name__ == '__main__':
	main()