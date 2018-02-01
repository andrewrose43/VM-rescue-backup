a = [1,1,2,3,5,8,13,21,34,55,89]
b = [1,2,3,4,5,6,7,8,9,10,11,12,13]

c = []

for vala in a:
	for valb in b:
		if (vala==valb):
			if (not vala in c):
				c.append(vala)

print(c)
