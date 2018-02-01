import sys

def ContainsOnlyWords(s):
	#Split s by whitespace.
	tokens = s.split()
	#If any token does not contain only letters, return False.
	for token in tokens:
		if not token.isalpha():
			return False
	return True

if __name__ == '__main__':
	if ContainsOnlyWords(input("Enter a bunch of words:")):
		print("Wat you entered contained only letters.")
	else:
		print ("Wat you entered contained non-letters.")
		
