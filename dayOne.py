import math

# summ = 0
temp = 0;
list1 = [];


def makeList():
	numlist = [] #create an empty list
	with open ('numbers.txt') as f:
		content = f.readlines() #get all of the file as strings
	print(content)
	for value in content:
		numlist.append(int(value))  #loop through each string in content and convert to an integer
		#and append to numlist
	print(numlist)
	return numlist
	# content = [x.strip() for x in content]
	#for i in range(1, 2):
	#	list1.append([x.strip() for x in content]);
	#	print list1[0]

# def printArr():
# 	for i in range(1, 100):
# 		print list1[i]

def calcSum(numlist):
	summ = 0
	#for i in range(len(numlist)):
	for value in numlist:
		temp = value
		temp = divide(temp)
		temp = roundDown(temp)
		temp = subTwo(temp)
		summ = summ + temp
	print summ
	return summ

def divide(d):
	d = d/3
	return d

def roundDown(r):
	math.floor(r)
	return r

def subTwo(s):
	s = s - 2
	return s



def main():
	numberList = makeList() #probably should pass the filename int that
	sum = calcSum(numberList)

main()