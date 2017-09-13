# Create a function called 'reverse_string' which takes a string as a parameter
# The function reverses it and returns with the reversed string

reverse = ".eslaf eb t'ndluow ecnetnes siht ,dehctiws erew eslaf dna eurt fo sgninaem eht fI"
# Solution 1
def reverse_string(text):
    return text[::-1]
print(reverse_string(reverse))
# Solution 2
def reverse_string(text):
    return "".join(reversed(reverse))
print(reverse_string(reverse))