import math
count = 0;


def make_list():
	num_list = []
	with open (r'/home/javanshir/Documents/PythonAdventure/dayTwo/input.txt') as file_name:
		file_content = file_name.readlines()
		print file_content
	for file_value in file_content:
		# read = int(file_value)
	 	num_list.append(int('file_value'))
		print num_list
		return num_list


def	zero (num_list):
	pass

def one(num_list):
	pass

def two(num_list):
	pass

def ninety_nine(num_list):
	pass

def op_code():
	op_code = {
		0 : zero,
		1 : one,
		2 : two,
		99 : ninety_nine,
	}

def main():
	make_list()

if __name__ == '__main__':
	main()
