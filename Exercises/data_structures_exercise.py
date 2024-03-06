'''


Exercise: Nested Loops and Data Structures

Create a list of dictionaries: Each dictionary in the list should represent a person. 

Include at least three dictionaries, and each should have keys for 'name', 'age', and 'hobbies', where 'hobbies' is a list of strings representing each person's hobbies.

Print the names and ages of all people: 

Use a for loop to go through the list of dictionaries. 

For each person, print their name and age.

Print everyone's hobbies: 

Still within the same loop, add an inner loop that iterates through each person's list of hobbies and prints each hobby.

Find and print the name of the person with the most hobbies: 

After the first loop, write a new loop to determine which person has the most hobbies and print that person's name and how many hobbies they have. 

If there are multiple people with the same highest number of hobbies, just print one of them.

'''

people = [ #dictionary of three people
    {'name': 'Alice', 'age': 30, 'hobbies': ['painting', 'reading', 'cycling']},
    {'name': 'Bob', 'age': 25, 'hobbies': ['coding', 'chess']},
    {'name': 'Charlie', 'age': 35, 'hobbies': ['running']}
]

max_hobbies = 0
person_with_most_hobbies = None

for person in people:
   name = person['name']
   age = person['age']
   print(name, age) #iterate through the dictionary and get the name and age
   hobbies = person['hobbies']
   print(hobbies)
   for hobby in hobbies:
       print(hobby)
    
for person in people: #go through the dictionary
       num_hobbies = len(person['hobbies']) #check the number of hobbies
       if num_hobbies > max_hobbies: 
           max_hobbies = num_hobbies #update max_hobbies
           person_with_most_hobbies = person #set person
if person_with_most_hobbies:
            print(f"Person with the most hobbies is {person_with_most_hobbies['name']} with {max_hobbies} hobbies")  # Corrected print statement
            #print person name with the most hobbies and the amount
    
       
        
        