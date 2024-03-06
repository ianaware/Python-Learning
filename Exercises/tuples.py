'''

Exercise
To put this into practice, try the following:

Create a tuple containing three different types of data (e.g., a string, an integer, and a float).

Print the second item in the tuple.

Try to change the value of the first item in the tuple (to see what happens).

Write a for loop to print each item in the tuple.


'''

my_tuple = (3.14, "Snow", 5)# create tuple with different data types

print(my_tuple[1]) #print second item in the tuple
# my_tuple[0] = "re" #this will give an error

#use for loop to print out tuple

for item in my_tuple: #start for loop with item as loop variable
    print(item) #print out the tuple items