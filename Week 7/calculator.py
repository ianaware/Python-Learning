'''
			§ Create a program that acts as a simple calculator. It should prompt the user to enter two numbers and then ask the user which operation (addition, subtraction, multiplication, division) they want to perform. Based on the user's choice, perform the operation on the two numbers and display the result. Here's what you should cover:
				□ Use input() to get user input.
				□ Convert string inputs to floats for calculation (consider what should happen if the user doesn't enter a number).
				□ Implement try-except blocks to handle division by zero and other potential value errors.
				□ Use if-elif-else statements to process the user's choice of operation.
				□ Print out the result in a user-friendly format.
					® Here is a basic structure (pseudo-code):
						◊ Get user inputs
						◊ Convert inputs to floats
						◊ Ask user for the operation
						◊ Perform the chosen operation using if-elif-else
						◊ Print the result
						◊ Use try-except for error handling (like division by zero)
'''
print("Welcome to the calculator\n")
print("Select what you want to do: \n")
print ("Type the following: \n")
print("Add - Add two numbers\n")
print("Subtract - Subtract two numbers\n")
print("Divide - Divide two numbers\n")
print("Multiply - Multiply two numbers\n")
print("Exit - exit the calculator")


user_input = input("Enter your choice: ")
while True:
    if user_input == 'Add' or user_input == 'add':
        print("Enter first number: ")
        input_1 = input()
        num_1 = int(input_1)
        print("Enter second number: ")
        input_2 = input()
        try:
            num_2 = int(input_2)
            print("The total is: ", num_1 + num_2)
            next_action = input("Type Continue to try again or Exit to quit\n")
            if next_action == "exit" or next_action == "Exit":
                print("Exiting the calculator")
                break
        except:
            print("Invalid input - try again")
        
    elif user_input == 'Subtract' or user_input == 'subtract':
        print("Enter first number: ")
        input_1 = input()
        num_1 = int(input_1)
        print("Enter second number: ")
        input_2 = input()
        try:
            num_2 = int(input_2)
            print("The total is: ", num_1 - num_2)
            next_action = input("Type Continue to try again or Exit to quit\n")
            if next_action == "exit" or next_action == "Exit":
                print("Exiting the calculator")
                break
        except:
                print("Invalid input - try again")
    elif user_input == "Divide" or user_input == "divide":
        print("Enter first number: ")
        input_1 = input()
        num_1 = int(input_1)
        print("Enter second number: ")
        input_2 = input()
        try:
            num_2 = int(input_2)
            print("The total is: ", num_1 / num_2)
            next_action = input("Type Continue to try again or Exit to quit\n")
            if next_action == "exit" or next_action == "Exit":
                print("Exiting the calculator")
                break
        except:
            print("Invalid input - try again")
    elif user_input == "Multiply" or user_input == "multiply":
        print("Enter first number: ")
        input_1 = input()
        num_1 = int(input_1)
        print("Enter second number: ")
        input_2 = input()
        try:
            num_2 = int(input_2)
            print("The total is: ", num_1 * num_2)
            next_action = input("Type Continue to try again or Exit to quit\n")
            if next_action == "exit" or next_action == "Exit":
                print("Exiting the calculator")
                break
        except:
            print("Invalid input - try again")
    elif user_input == "Exit" or user_input == 'exit':
        print("Exiting the calculator - Goodbye!")
        break