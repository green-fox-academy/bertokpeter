# Create a simple calculator application which does read the parameters from the prompt 
# and prints the result to the prompt. 

# It should support the following operations: 
# +, -, *, /, % and it should support two operands. 

# The format of the expressions must be: {operation} {operand} {operand}. 
# Examples: "+ 3 3" (the result will be 6) or "* 4 4" (the result will be 16)

# You should use the input() function to accept user input
# It should work like this:

# Start the program
# It prints: "Please type in the expression:"
# Waits for the user input
# Print the result
# Exit
print("Please type in the expression:")
players_input = input()
operator = players_input[0]
operand1 = int(players_input[2])
operand2 = int(players_input[4])
def calculator(operation,operan1,operan2): 
    if operation == "+":
        return operan1 + operan2
    if operation == "-":
        return operan1 - operan2
    if operation == "*":
        return operan1 * operan2
    if operation == "/":
        return operan1 / operan2
    if operation == "%":
        return operan1 % operan2
calculation = calculator(operator,operand1,operand2)
print(calculation)