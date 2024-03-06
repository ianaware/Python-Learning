'''

Creates a tuple named my_tuple containing the following elements: 3.14, 'apple', 25, 'blue'.

Prints the entire tuple.

Accesses and prints the second element from the tuple.

Attempts to change the third element of the tuple to 30 (to understand the immutability of tuples).

Counts and prints how many times 'apple' appears in the tuple.

'''

my_tuple = (3.14, "apple", 25, "blue", "apple") #tuples use () NOT {}
print(f"This is a tuple {my_tuple}")
print(f"The second element is {my_tuple[1]}")
new_tuple = (30,)
my_tuple = my_tuple + new_tuple
print(f"The new tuple is {my_tuple}") #the original tuple now contains 30
print(f"The word 'apple' appears: {my_tuple.count('apple')}")