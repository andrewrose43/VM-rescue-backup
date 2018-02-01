str = input("Please enter anything you like")
count = 0
pal = True
for val in str[0:int(len(str)/2)]:
	count = count - 1
	if (not val == str[count]):
		pal = False
		break
if (pal):
	print ("You entered a palindrome!")
else:
	print ("You did not enter a palindrome. LAME!")
