# Create a method that decrypts reversed-order.txt
rev_ordered_file = "week-03/day-01/reversed-order.txt"
def reverse_order(file_name):
    line_list = []
    with open(file_name, "r") as f1:
        for line in f1:
            line_list.append(line)
    for i in line_list[::-1]:
        print(i, end='')
reverse_order(rev_ordered_file)