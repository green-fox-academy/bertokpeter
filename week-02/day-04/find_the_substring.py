# Find part of an integer

# Create a function that takes two strings as a parameter
# Returns the starting index where the second one is starting in the first one
# Returns -1 if the second string is not in the first one
# Example

# input: "this is what I'm searching in", "searching"
# output: 17
searching_in = "this is what I'm searching in"
to_search = "searching"
def substring_finder(text1,text2):
    if text2 in text1:
        return text1.find(text2)
    else:
        return -1
print(substring_finder(searching_in,to_search))