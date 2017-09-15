input_number = int(input("Please enter the number of people who play here: "))
def create_list(number):
    number_list = []
    for i in range(1,number+1):
        number_list.append(i)
    return number_list
def josephus(number):
    number_list = create_list(number)
    length = len(number_list)
    while len(number_list) > 1:
        for i in range((length+1)//2):
            if number_list[i] == number_list[len(number_list)-1]:
                number_list.remove(number_list[0])
                break
            else:
                number_list.remove(number_list[i+1])
                if number_list[i] == number_list[len(number_list)-1]:
                    break
    return number_list
print(josephus(input_number))