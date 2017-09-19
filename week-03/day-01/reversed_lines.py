# Create a method that decrypts reversed-lines.txt
reversed_file = "week-03/day-01/reversed_lines.txt"
def reverse(file_name):
    with open(file_name, "r") as f1:
        for line in f1:
            print(line[::-1], end='')
reverse(reversed_file)