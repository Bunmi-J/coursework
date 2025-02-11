# Write a Python program that functions as a simple calculator. The program should:
# Ask the user to enter two numbers.
# Ask the user to choose an operation: Addition (+), Subtraction (-), Multiplication (*), or Division (/).
# Perform the selected operation and display the result.
# Handle division by zero errors gracefully.
# Allow the user to perform multiple calculations until they choose to exit.

# get inputs from user

first_num = input('Enter a random number: ')
second_num = input('Enter a random number: ')
# convert string input to interger
first_to_int = int(first_num)
second_to_int = int(second_num)
# choose numeric operator
choice_of_operator = input('choose an operation: Addition (+), Subtraction (-), Multiplication (*), or Division (/)')
# perform operation
try:
    
    if choice_of_operator == '+':
        result = (first_to_int + second_to_int)
    elif choice_of_operator == '_':
        result = (first_to_int - second_to_int)
    elif choice_of_operator == '*':
        result = (first_to_int * second_to_int)
    elif choice_of_operator == '/':
        result = (first_to_int / second_to_int)
        
    else:
        print('operation not recognised')
except ZeroDivisionError:
    result = 0       
print('The result is {}'.format(result))
