# Create a method that find the 5 most common lottery numbers otos.csv
lottery_file = "bertokpeter/week-03/day-01/otos.csv"

def replace_comma(file_name):
    with open(file_name, "r") as file:
        text = file.read()
    text = text.replace(";",",")
    with open(file_name, "w") as file:
        file.write(text)
replace_comma(lottery_file)

# def five_most_frequent():
#     pass