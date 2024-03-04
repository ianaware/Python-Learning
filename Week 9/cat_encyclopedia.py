'''

In this program, you could:

Create a dictionary for each cat, with keys like 'name', 'age', 'breed', and 'color'.

Allow the user to add new cats to a list, view all cats in the list, and search for cats by name.

Implement functions for each of these actions: add_cat(), view_cats(), and search_cats().

'''

Cats = [] #empty list

quit_program = False

while quit_program == False:
    
    print("Welcome to the cat encyclopedia")
    print("Please choose an option: ")
    print(" '1' - Add a new cat to the list")
    print(" '2' - View all cats in the list")
    print(" '3' - Search for a cat by name")
    print(" 'q' - Quit the program")
    
    user_input = input() #get user input
    
    if user_input == 'q' or user_input == 'Q':
        quit_program = True
        print("The program will quit meow")
        
    elif user_input == '1':
        print("You have chosen to enter a new cat to the list")
        while True:
            print("Enter the cat name: ")
            cat_name = input().strip()
            if cat_name != '':
                break
            else:
                print("The cat name cannot be empty.  Please enter a valid name")
        while True:
                print("Enter the cat's age: ")
                cat_age = input().strip()
                try:
                    cat_age_int = int(cat_age)
                    break
                except ValueError:
                    print("Enter a valid cat age as an integer")
        while True:
                print("Enter the cat's breed: ")
                cat_breed = input().strip()
                if cat_breed != '':
                    break
                else:               
                    print("The cat breed cannot be empty")
        while True:
            print("Enter the cat's favourite toy: ")
            cat_toy = input().strip()
            if cat_toy != '':
                    break
            else:               
                print("The cat's favourite toy cannot be empty")
        while True:
            print("Enter the cat's colour: ")
            cat_colour = input().strip()
            if cat_colour != '':
                    break
            else:               
                print("The cat colour cannot be empty")
        saved_cat = {
            "name": cat_name,
            "age": cat_age_int,
            "breed": cat_breed,
            "favourite_toy": cat_toy,
            "colour": cat_colour          
            } #create cat dictionary
        Cats.append(saved_cat) #Add dictionary data to list 
        print(f"Name: {cat_name}, Age: {cat_age_int}, Breed: {cat_breed}, Favourite Toy: {cat_toy}, Colour: {cat_colour} has been added successfully")   
    
    elif user_input == "2":
        print("You have chosen to view all cats in the list")
        for Data in Cats:
            print(f"{Data['name']}, {Data['age']}, {Data['breed']}, {Data['favourite_toy']}, {Data['colour']}") #print cat details using ditionary information
    
    elif user_input == '3':
        print("Enter name of cat to search for: ")
        cat_search = input() 
        print("You have chosen to look up:", cat_search)
        cat_found = False #set variable to track if cat is found
        for Data in Cats:
            if cat_search == Data['name']:
                print(f"{cat_search}'s details are: {Data['name']}, {Data['age']}, {Data['breed']}, {Data['favourite_toy']}, {Data['colour']}") #print cat details using ditionary information
                cat_found = True #set variable to True as cat is found
        if cat_found ==False:
                print(f"No information available for {cat_search}")  
        
    else:
        print("Enter a valid option")
    