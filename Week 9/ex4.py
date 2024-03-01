'''

Exercise: Counting Words in Names

Objective: Write a Python program that reads a series of names (first and last name) entered by the user, splits each name into first name and last name, and then counts how many names there are in total. 

Additionally, count how many unique first names and last names there are.

'''

first_names = {}
last_names = {}

names_string = input("Enter names separated by a comma ")
names_list = names_string.split(',')  # This splits the input string by commas into a list of names.



for name in names_list:
    cleaned_name = name.strip() #this gives the name
    split_name = cleaned_name.split() #split name in to two sections
    first_name = split_name[0] #get first name
    last_name = split_name[1] #get second name
    
    if first_name in first_names: #if first name exists in dictionary (first_names)
        first_names[first_name] +=1 #increase the count
    else:
        first_names[first_name] = 1 #add the first name with a count of 1 if it's not already in the dictionary
    
    if last_name in last_names: #if last name exists in dictionary (last_names)
        last_names[last_name] += 1 #increase the count

# Print each first name and its count
for first_name, count in first_names.items():
    print(first_name, count)

# Print each last name and its count
for last_name, count in last_names.items():
    print(last_name, count)

