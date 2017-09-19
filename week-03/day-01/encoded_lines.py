# Create a method that decrypts encoded-lines.txt
import string
encoded_file = "week-03/day-01/encoded_lines.txt"
def decrypt(file_name):
    decoded_line = ""
    with open(file_name, "r") as f1:
        for line in f1:
            for char in line:


def swap(char):
    decoder = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ[,-./'(*+"
    actual_index = decoder.index(char)
    return 	string.ascii_lowercase[actual_index-1]


decrypt(encoded_file)
str = "bmnb"
out = ""
for char in str:
	out += swap(char)
print(out)