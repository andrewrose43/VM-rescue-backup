number = int(input("Please enter a positive integer.\n"))
odd = number % 2
if (odd):
	print("Your number is odd.")
else if (not number % 4):
	print("Your number is a multiple of 4.")
else:
	print("Your number is even.")
