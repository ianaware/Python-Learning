'''

Exercise: Create a Python script that performs basic list operations.

Your script should do the following:

Create a list called fruits containing the strings "apple", "banana", and "cherry".
Add "orange" to the end of the fruits list.
Remove "banana" from the fruits list.
Print out the index of "cherry" in the fruits list.
Add "lemon" to the second position in the list.
Print the length of the fruits list.
Print out the entire fruits list to see the final result.

'''

#Note, as this is a list exercise, no need for a loop!

fruits = ["apple", "banana", "cherry"]

print("The current fruit list is: ", fruits)
print("Now we add orange to the list ")

fruits.append("orange")

print("The new fruit list is ", fruits)
print("Now we will remove banana from the list ")

fruits.remove("banana")

print("The updated fruits list is: ", fruits)
print("The index of cherry is: ",fruits.index("cherry"))
print("Now we will add lemon to position 2 of the list")

fruits.insert(2, "lemon")

print("The updated fruits list is: ", fruits)
print("The length of the fruits list is: ", len(fruits))
print("The final fruits list is: ", fruits)
