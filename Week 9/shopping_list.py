'''

Objective: Write a Python script that will help organize a shopping list.

Initialize Your List: Start by creating an empty list named shopping_list.

Populating the List: Ask the user to input items for the shopping list one at a time. 

After each item is input, add the item to the shopping_list. 

Continue asking for items until the user types "done". 

Hint: You can use a loop and the input() function for this part.

Sorting the List: Once the user is done entering items (they've typed "done"), sort the shopping_list in alphabetical order. Hint: Python lists have a built-in method to sort themselves.

Printing the List: Print out each item in the sorted shopping_list one by one. 

Hint: Use a loop to iterate through the sorted list and print() each item.

Enhancements (Optional):

Before adding an item to the list, check if it's already there. If it is, print a message like "Item already in list" and don't add it again.

Allow the user to specify how many of each item they need. Instead of a list of strings, you might need a list of tuples like ('apples', 3).


'''

shopping_list = [] #Initialise empty list

print("Welcome to the shopping list ")

while True: # start loop
    user_input = input ("Enter the item and the quantity and press Enter or type 'done' to quit\n") 
    print("Or type 'Done' to exit\n")
    
    if user_input.lower() == 'done':
        break 
    
    split_input = user_input.split() #split the user input into item, quantity
    if len(split_input) != 2: #checks if there are two values
        print("Please enter an item and a quantity")
        continue
    
    item, quantity_str = split_input #split the list in to item string and quantity string
    
    try:
        quantity = int(quantity_str) #convert quantity string to integer
    except ValueError: #check if value is correct or not
        print("Enter a valid quantity")
        continue
    
    item_tuple = (item, quantity) #creat tuple with item and quantity
    if any(item == existing_item[0] for existing_item in shopping_list):
        print("Item is already in the list")
    
    else:   
        shopping_list.append(item_tuple) #add the tuple to the shopping list
        print(f"Item Name: {item} with quantity {quantity} has been added to the cart successfully")  
    
print("Final shopping list:", shopping_list)
shopping_sorted = sorted(shopping_list)
for items in shopping_sorted:
    print(f"Your purchased item: {item}, Quantity: {quantity}")
    
 
        
        
    