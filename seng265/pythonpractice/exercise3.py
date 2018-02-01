l = [1,1,2,3,5,8,13,21,34,55,89]
num = int(input("Choose a number: "))
new_list = []
for element in l:
	if (element < num):
		new_list.append(element)
print (new_list)
