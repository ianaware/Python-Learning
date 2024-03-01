'''
Program: Favorite Color Counter

Objective: Write a Python program that asks multiple users for their favorite color, then counts and displays the number of votes each color received.

Here's a step-by-step guide to what your program should do:

Collect Color Preferences:

Ask the user to input their favorite colors, separated by commas (e.g., "red, blue, green"). Allow multiple users to enter their preferences in a single input for simplicity.

Prepare for Counting:

Initialize an empty dictionary named color_count that will store each color as a key and the number of times it has been chosen as its value.

Process Each Color:

Split the input string into individual color names.
Loop through the list of colors, and for each color, update the color_count dictionary to keep track of how many times each color appears.

Display the Results:

After all inputs have been processed, print out each color and the number of votes it received.

'''

colour_count = {} #empty dictionary

colour_input = input("Enter your favourite colours separated by commas (e.g., red, blue, green): ")
colour_list = colour_input.split(',')

for colour in colour_list:
    colour = colour.strip()
    if colour in colour_count: #if colour exists in dictionary (colour_count)
        colour_count[colour] +=1 #increase the count
    else:
        colour_count[colour] = 1 #add the word with a count of 1 if it's not already in the dictionary

for colour, count in colour_count.items(): #print each colour and its count
    print(colour, count) #output each colour with its count
    
    