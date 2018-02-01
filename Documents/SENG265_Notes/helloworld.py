import sys
import os.path # file structures

#you can import other stuff too
import my_module
# a module is an organization of code which 

if __name__ == "__main__":
	print("{} was run from the command line".format(__name__))
else:
	print("nope")

def add10(x): #this is how you start a function
	return x+10

if __name__ == "__main__":

print name()
print(add10(5))
