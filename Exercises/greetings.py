'''

Exercise: Create a Python script that generates a personalized greeting.

The script should:

Ask the user for their name.
Ask the user for their favorite color.
Output a personalized greeting that includes their name and compliments their favorite color. 

For example, if the user inputs "Alice" as their name and "blue" as their favorite color, the script could say: "Hello, Alice! Blue is such a serene and beautiful color!"

'''

name_input = input("Enter your name: ") #Get user input and store as name
colour_input = input ("Tell me your favourite colour: ") #Get user input and store as colour 
if name_input and colour_input:
    print(f"Nice to meet you, {name_input}. {colour_input} is such a great colour! ") #print greeting and use name and colour
else:
    print("Invalid input")