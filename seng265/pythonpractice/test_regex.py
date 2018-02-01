import re
import sys

instr = input("Please enter something.")
if (re.search('[A-Za-z0-9\-_]{5,10}', instr)):
	print("We have a match!")
else:
	print("Not a match.")
