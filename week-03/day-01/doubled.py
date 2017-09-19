# Create a method that decrypts the duplicated-chars.txt
crypted_file = "week-03/day-01/duplicated-chars.txt"
def decrypt(file_name):
    new_file = ""
    with open(file_name, "r") as f1:
        for line in f1:
            for i in range(len(line)-1):
                if line[i] == line[i+1]:
                    new_file = new_file + line[i]    
            print(new_file)
            new_file = ""
decrypt(crypted_file)