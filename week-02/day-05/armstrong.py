input_number = int(input("Please enter your number here: "))
def create_list(number):
    string_number = str(number)
    number_list = []
    for i in string_number:
        number_list.append(int(i))
    return number_list
def armstrong(number):
    armstrong_list = create_list(number)
    sum_list = []
    for i in armstrong_list:
        sum_list.append(i**len(armstrong_list))
    if sum(sum_list) == number:
        print(str(number) + " is an armstrong number")
    else:
        print(str(number) + " isn't an armstrong number")
armstrong(input_number)