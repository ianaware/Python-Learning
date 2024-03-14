numbers = [10, 5, 7, 2, 1]
print("List content:", numbers)  # Printing original list content.
numbers[1] = numbers[4]
print("Updated list contents:", numbers)
print("The length of the list is:", len(numbers))
del (numbers[1])
print("The new length of the list is:", len(numbers))
#print(numbers[5]) #Will error as out of range

'''
And now we want the value of the fifth element to be copied to the second element - can you guess how to do it?

'''