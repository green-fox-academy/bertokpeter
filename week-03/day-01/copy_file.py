# Write a function that copies a file to an other
# It should take the filenames as parameters
# It should return a boolean that shows if the copy was successful
first_file = "week-03/day-01/my-file.txt"
second_file = "week-03/day-01/multiple.txt"
def copy_file(file_1, file_2):
    with open(file_1, "r") as f1:
        f1_content = f1.read()
    with open(file_2, "w") as f2:
        f2.write(f1_content)
copy_file(first_file, second_file)