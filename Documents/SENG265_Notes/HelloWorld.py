class MyException(Exception): # inheriting from Exception
	pass

class HelloWorld:

        def __init__(self, input_str):
                self._str = input_str # private variables are denoted with a single underscore
                self._font_size = 12
		self.__class__.counter = 0

        def set_str(self, input_str):
                self._str = input_str

        def get_str(self):
                return self._str

        def set_font_size(self, font_size=None):
		if font_size:
                	self._font_size = font_size
		else:
			return self._font_size

        def print_str(self):
                print(self._str)

	def count(self):
		return self.__class__.counter

	def print_dict(self, **kwargs): # using a dictionary
		print(kwargs)# just prints the whole dictionary
		for k, v in kwargs.items():
			print(k,v) # just prints the key and value

	def add(self, int1, int2=0, int3=200): # 0 is the default val of int2 if it is not supplied. You can't put non-default-having arguments after default-having arguments
		return int1 + int2 + int3

	def helper(self, arg):
		if arg < 10:
			raise MyException("Oh no!")

	def divide(self, int1, int2):
		try:
			self.helper()
			int2[4]=3
			return int(int1)/int(int2)
		except ZeroDivisionError as e:
			print("Error", e)
			return0
		except ValueError as e: #might be caused bysupplying the wrong type of variable (a string where an int should be, for example)
			print("Error", e)
			return 11
		except MyException as e:
			print("Custom Error:", e)
			import sys
			sys.exit(1)

# there are a ton of different errors

if __name == "__main":
	hw = HelloWorld("Hello")
	total1 = hw.add(10,100)
	total2 = hw.add(10)
	total3 = hw.add(10, int3=500)
	print("Total 1: {}".format(total))
	res = hw.divide(10, 0)
	print("Result: {}".format(res))
