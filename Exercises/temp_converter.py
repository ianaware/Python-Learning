'''

Exercise: Create a Simple Temperature Converter

Write a Python program that converts temperatures from Fahrenheit to Celsius and vice versa. Your program should:

Ask the user to enter a temperature followed by the unit (either F for Fahrenheit or C for Celsius). For example, the user could enter "32F" or "0C".
Convert the entered temperature to the opposite unit (Fahrenheit to Celsius or Celsius to Fahrenheit).
Print the converted temperature in the correct unit.


'''

        
while (True):
    user_input = input("Press 'c' to convert to Celsius or 'f' to convert to Fahrenheit or type 'quit' to exit\n")

    if user_input.lower() == 'quit':
        print("Exiting program")
        break
        
    if user_input.lower() == 'c':
        print("You have chosen to convert from Fahrenheit to Celsius") #Start conversion
        print("Enter value to convert: ")
        fahrenheit_input = input()
        try:
            fahrenheit_float = float(fahrenheit_input)
            print(f"The value of {fahrenheit_float} Fahrenheit to Celsius is:", (fahrenheit_float - 32) / 1.8 )
        except ValueError:
            print("Invalid input ")
    elif user_input.lower() == 'f':
        print("You have chosen to convert from Celsius to Fahrenheit")
        print("Enter value to convert from Celsius to Fahrenheit: ")
        celsius_input = input()
        try:
            celsius_float = float(celsius_input)
            print(f"The value of {celsius_float} Celsius in Fahrenheit is:", (celsius_float * 1.8) + 32 )
        except ValueError:
            print("Invalid input ")

    else:
        print("Invalid input ")
