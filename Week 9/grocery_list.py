'''

Objective:

Write a Python program that asks the user to enter grocery items they need to buy, then categorizes these items into different sections of the store, and finally prints out the items sorted by category.

Instructions:

Collect Grocery Items:

Ask the user to enter the names of grocery items they need to buy, separated by commas (e.g., "apples, bread, chicken, milk, lettuce").

Allow the user to enter as many items as they wish.

Categorize Items:

For simplicity, let's assume there are three categories: 'Fruits', 'Bakery', and 'Dairy & Meat'.

Create a dictionary where each category is a key, and the value is a list of items belonging to that category.

Sort and Print the Grocery List:

For each category, sort the items alphabetically and print them out under their respective category headings.

'''
Categories = {
    'Fruits': [],
    'Bakery': [],
    'Dairy & Meat': []
}

item_categories = {
    'apples': 'Fruits',
    'bread': 'Bakery',
    'milk': 'Dairy & Meat'
}

print("Enter your shopping list, separate each item with a comma")
user_input=input()

items = user_input.split(',') #split items by comma
for item in items:
    item = item.strip().lower()#remove whitespace
    category = item_categories.get(item) #get the category of the item, None if not found

    if category: #if item has category
        Categories[category].append(item) #add to category
    else:
    # Optional: Add unlisted items to a 'Miscellaneous' category
        if 'Miscellaneous' not in Categories:
            Categories['Miscellaneous'] = []  # Create the category if it doesn't exist
        Categories['Miscellaneous'].append(item)  # Add the item to 'Miscellaneous'

for category, items_in_category in Categories.items():
    print(f"{category}:") #print category name
    for item in sorted(items_in_category):
        print(f" - {item}")
    print()  # Print a newline for better readability between categories
    

