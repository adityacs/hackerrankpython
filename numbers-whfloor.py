#Find Cost of Tile to Cover W x H Floor 
#Calculate the total cost of tile it would take to cover a floor plan of 
#width and height, using a cost entered by the use

def calculate():
	total_cost = cost * width * height
	return total_cost

def main():
	global width, height, cost
	width = float(raw_input("Enter width of the floor: "))
	height = float(raw_input("Enter height of the floor: "))
	cost = float(raw_input("Enter cost: "))
	print calculate()

if __name__ == '__main__':
	main()


