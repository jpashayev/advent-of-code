import math

temp = 0;

def make_list():
	num_list = [] #create an empty list
	with open (r'/home/javanshir/Documents/PythonAdventure/dayOne/input.txt') as f:
		content = f.readlines() #get all of the file as strings
	for value in content:
		num_list.append(int(value))  #loop through each string in content and convert to an integer
		#and append to numlist
	return num_list
	# content = [x.strip() for x in content]
	#for i in range(1, 2):
	#	list1.append([x.strip() for x in content]);
	#	print list1[0]
# def printArr():

# 	for i in range(1, 100):
# 		print list1[i]

def calc_sum(num_list):
	summ = 0
	#for i in range(len(numlist)):
	for value in num_list:
		temp = value
		temp = fuel_module(temp)
		summ = summ + temp
	print summ
	return summ

def fuel_module(d):
	sum_val = 0;
	while d >= 9:
		d = d/3
		math.floor(d)
		d = d - 2
		sum_val = sum_val + d
	return sum_val

def main():
	number_list = make_list()
	sum = calc_sum(number_list)

if __name__ == '__main__':
	main()