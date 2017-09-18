# Open a file called "my-file.txt"
# Write your name in it as a single line
# If the program is unable to write the file,
# then it should print an error message like: "Unable to write file: my-file.txt"
try:
    my_file = open("week-03/day-01/my-file.txt", "w")
    my_file.write("Bertok Peter")
    my_file.close()
except IOError:
    print("Unable to write file: " + my_file)