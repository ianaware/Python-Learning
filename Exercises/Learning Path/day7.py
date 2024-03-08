'''
Day 7: Sets and Tuples
• Create a set containing some colors and print it.
• Write a program that converts a list into a tuple and prints the immutable tuple.


'''

colour_set = {"Red", "Orange", "Green", "Blue", "Purple"} #create the set using {}

print(f'The set contents are: {colour_set}') #print out the set, it will display values randomly

my_list = [1, 20, 446, 23] #create a list of numbers

my_tuple = tuple(my_list) #use tuple() to convert

print(f'This tuple contains a list {my_tuple}')

