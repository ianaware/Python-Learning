'''

Exercise: Favorite Colors

Create a Python program that does the following:

Ask three friends for their favorite colors and store their responses in a dictionary. 
In this dictionary, the keys should be the friends' names, and the values should be their favorite colors.

After collecting the information, the program should ask for the name of one of the friends and display their favorite color.

Steps:

Prompt the user to enter the names and favorite colors of three friends.
Store this information in a dictionary.
Ask the user which friend's favorite color they want to know.
Display the favorite color of the requested friend.


'''

friends_data = {} #empty dictionary

friend1_name = input("Enter the name of friend one :") #get friend 1 name
friend1_colour = input("Enter the favourite colour of friend one: ") #get friend 1 colour
friends_data[friend1_name] = friend1_colour #add values to dictionary as key | value

friend2_name = input("Enter the name of friend two :") #get friend 1 name
friend2_colour = input("Enter the favourite colour of friend two: ") #get friend 1 colour
friends_data[friend2_name] = friend2_colour #add values to dictionary as key | value

friend3_name = input("Enter the name of friend three :") #get friend 1 name
friend3_colour = input("Enter the favourite colour of friend three: ") #get friend 1 colour
friends_data[friend3_name] = friend3_colour #add values to dictionary as key | value

user_input = input("Which friend do you want to look up? ")

if user_input in friends_data: #check if user input is a key in the friends_data dictionary
    print(f"{user_input}'s favourite colour is {friends_data[user_input]}")
else:
    print(f"No information available for {user_input}")


