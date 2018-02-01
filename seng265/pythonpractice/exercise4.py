num = int(input("Enter a positive integer\n"))
i = range(1,num)
for val in i:
	if (not(num/val)%1):
		print(val)
