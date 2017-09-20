# Find the substring in the list

# Create a function that takes a string and a list of string as a parameter
# Returns the index of the string in the list where the first string is part of
# Returns -1 if the string is not part any of the strings in the list
# Example

string_list = ["this", "is", "what", "I'm", "searching", "in"]
text = "ching" 
# output: 4
def find_substring(string_list, string):
    string_index = []
    for i in range(len(string_list)):
        if string in string_list[i]:
            string_index.append(i)
    return string_index
print(find_substring(string_list,text))