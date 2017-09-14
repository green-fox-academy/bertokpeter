# Unique - remove the duplicates

# Create a function that takes a list of numbers as a parameter
# Returns a list of numbers where every number in the list occurs only once
# Example

input = [1, 11, 34, 11, 52, 61, 1, 34]
output: [1, 11, 34, 52, 61]
def unique(input_list):
    output = list(set(input_list))
    return output
print(unique(input))
def unique1(input_list):
    output = []
    for i in input_list:
        if not i in output:
            output.append(i)
    return output
print(unique1(input))