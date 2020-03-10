
        sum_val = sum_val + dimport math

def make_list():
    num_list = []
    with open ('input.txt') as f:
        content = f.readlines()
    for value in content:
        num_list.append(int(value))
    return num_list

def calc_sum(num_list):
    summ = 0
    for value in num_list:
        temp = value
        temp = fuel_module(temp)
        summ = summ + temp
    print "The answer is: "
    print summ
    return summ

def fuel_module(d):
    sum_val = 0;
    while d >= 9:
        d = d//3
        d = d - 2
    return sum_val

def main():
    number_list = make_list()
    calc_sum(number_list)

if __name__ == '__main__':
    main()
