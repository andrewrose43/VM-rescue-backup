class textshifter:
	
	def __init__(self, key):
		self._shift = key

	def encrypt(self, text): # note: only works on caps
		newtext = ""
		for c in text:
			if ((ord(c)+self._shift) > 90):
				newtext	+= chr(ord(c)+self._shift-26)
			else:
				newtext += chr(ord(c)+self._shift)
		print(newtext)


	# ord('z') = 112 which is the ASCII value of z
	# chr(122) = 'z'
