'''
Exercise

Let's practice what you've learned about lists. Here's a simple exercise for you:

Create a list of your favorite fruits.
Print the second fruit in the list.
Add a new fruit to the end of the list.
Change the last fruit to "Strawberry".
Use a for loop to print each fruit in the list.

'''

fruits = ["Banana", "Apple", "Grapefruit", "Orange", "Pear"] #create list

print(f'The second fruit in the list is {fruits[1]}') #get second fruit value
fruits.append('Durian') #add another fruit
print(fruits)
fruits[-1] = 'Strawberry' #this will make sure strawberry is the last fruit in the list as -1 means end of list
print(fruits)

#create for loop

for fruit in fruits: #loop through fruits
    print(fruit) #print values