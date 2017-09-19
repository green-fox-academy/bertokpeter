# Create a method that decrypts encoded-lines.txt
encoded_file = "week-03/day-01/encoded_lines.txt"
def decrypt(file_name):
    decoded_line = ""
    with open(file_name, "r") as f1:
        for line in f1:
            for char in line:
                decoded_line += swap(char)
            print(decoded_line, end='')
            decoded_line = ""

def swap(char):
    decoder = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ[,-./'(*+!\""
    if char in decoder:
        actual_index = decoder.index(char)
        return 	decoder[actual_index-1]
    else:
        return char

decrypt(encoded_file)