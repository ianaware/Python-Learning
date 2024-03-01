'''

Exercise: Simple Phone Book

Create a Python program that allows a user to do two things:

Add a new contact (name and phone number) to a phone book.

Look up a contact's phone number by their name.

Steps:
		Start with an empty dictionary called phone_book.
		Allow the user to choose between adding a new contact or looking up an existing one.
		If adding, ask for the contact's name and phone number, then add them to the dictionary.
		If looking up, ask for the contact's name and display their phone number.
		Repeat the process until the user decides to quit.

'''
phone_book = {} #empty dictionary

while True: #start loop
    print("Welcome to the phone book. \n")
    print("Please choose an option:\n ")
    print("1 - Add a new contact:\n ")
    print("2 - Look up a new contact: \n")
    print("Type 'exit' to quit\n")

    user_input = input() #read user input
    
    if user_input.lower() == 'exit':
        print("Exiting the program")
        break

#Choose to add a contact    
    
    elif user_input == '1':
            print("You have chosen to add a new contact.\n ")
            print("Enter the contact name ")
            contact_name = input()
            print("You have set the contact name as:", contact_name)
            print("Enter the contact number: ")
            contact_number = input()
            try:
                contact_int = int(contact_number)
                if len(contact_number) == 5:
                    print("You have entered the contact number as: ", contact_number)
                    phone_book[contact_name] = contact_number #add values to dictionary as key | value
                    print("The contact data has been added successfully.\n ")
                else:
                    print("Contact numbers must be five digits\n ")
            except ValueError:
                print("Enter a correct value ")
    
    elif user_input == '2':
            print("You have chosen to look up new contact.\n ")
            print("Enter the contact name to look up: ")
            contact_name = input()
            print("You have chosen to look up:", contact_name)
            if contact_name in phone_book: #check if user input is a key in the phone book dictionary
                print(f"{contact_name}'s phone number is {phone_book[contact_name]}")
            else:
                print(f"No information available for {contact_name}")  
    else:
        print("Enter a valid option ")




