# Sort that list

# Create a function that takes a list of numbers as parameter
# Returns a list where the elements are sorted in ascending numerical order
# Make a second boolean parameter, if it's true sort that list descending
# Example

numbers = [34, 12, 24, 9, 5, 65, 34, 78, 77]
descend = input("Do you want your list to descend? (Yes/No): ")
if descend == "Yes":
    descend = True
elif descend == "No":
    descend = False
def bigger(number1, number2):
    return number1 > number2
def swap(number1):
    second = number1 + 1
    numbers[number1], numbers[second] = numbers[second], numbers[number1]
def sorting(input_list,descending):
    for i in range(len(numbers)-1):
        for j in range(len(numbers)-1-i):
            if not descending:   
                if bigger(input_list[j], input_list[j+1]):
                    swap(j)
            else:
                if not bigger(input_list[j], input_list[j+1]):
                    swap(j)
    print(input_list)
sorting(numbers, descend)