input_number = int(input("Please enter the number of people who play here: "))
def create_list(number):
    number_list = []
    for i in range(1,number+1):
        number_list.append(i)
    return number_list
def josephus(number):
    number_list = create_list(number)
    i = 0
    while len(number_list) > 1:
        if i == len(number_list)-1:
            number_list.remove(number_list[0])
            i = 0
        else:
            number_list.remove(number_list[i+1])
            if i == len(number_list)-1:
                i = 0
            else:
                i += 1
    return number_list
print(josephus(input_number))