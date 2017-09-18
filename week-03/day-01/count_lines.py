# Write a function that takes a filename as string,
# then returns the number of lines the file contains.
# It should return zero if it can't open the file, and
# should not raise any error.
my_file = "week-03/day-01/my-file.txt"
def line_counter(file_name):
    try:
        file = open(file_name, "r")
        print(len(file.readlines()))
        file.close()
    except IOError:
        print("Unable to read file: " + file_name)
    except:
        print("Error")
line_counter(my_file)