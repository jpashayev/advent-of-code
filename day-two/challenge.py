def convertStrListToIntList(str_list):
	num_list = []
	for val in str_list:
		num_list.append(int(val))
	return num_list


def make_list():
	with open('input.txt', "r") as file_name:
		file_content = file_name.readline()
	num_list = file_content.split(',')
	num_list = convertStrListToIntList(num_list)
	return num_list


def one(x, num_list):
	val_x = num_list[x+1]
	val_y = num_list[x+2]
	temp_one = num_list[val_x]
	temp_two = num_list[val_y]
	temp_three = temp_one + temp_two
	position = num_list[x+3]
	num_list[position] = temp_three
	return num_list

def two(x, num_list):
	val_x = num_list[x+1]
	val_y = num_list[x+2]
	temp_one = num_list[val_x]
	temp_two = num_list[val_y]
	temp_three = temp_one * temp_two
	position = num_list[x+3]
	num_list[position] = temp_three
	return num_list

def main():
	num_list = make_list()
	booly = True
	temp = 0
	while booly:
		if num_list[temp] == 1:
			num_list = one(temp, num_list)
			temp = temp + 4
		elif num_list[temp] == 2:
			num_list = two(temp, num_list)
			temp = temp + 4
		elif num_list[temp] == 99:
			booly = False
		else:
			pass
	print "The answer is: "
	print	num_list[0]

if __name__ == '__main__':
	main()
