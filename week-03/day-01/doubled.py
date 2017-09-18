# Create a method that decrypts the duplicated-chars.txt
crypted_file = "week-03/day-01/duplicated-chars.txt"
def decrypt(file_name):
    new_file = ""
    with open(file_name, "r") as f1:
        whole_file = f1.read()
    for i in range(len(whole_file)-1):
        if whole_file[i] == whole_file[i+1]:
            pass
        else:
            new_file = new_file + whole_file[i]
    print(new_file)
decrypt(crypted_file)