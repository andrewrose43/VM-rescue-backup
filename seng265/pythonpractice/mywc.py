import sys

def main():
	num_chars = 0
	num_words = 0
	num_lines = 0

	for line in sys.stdin: #note that stdin is automatically divided into lines
		num_lines = num_lines + 1
		num_chars += len(line)
		line = line.strip() #take away newlines
		words = line.split() #str.split(str="", num.string.count(str)) by default, split() splits the entire line by spaces
		num_words += len(words)
	
	print(num_lines, num_words, num_chars)

if __name__ == "__main__":
	main()
