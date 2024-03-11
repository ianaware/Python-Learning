'''
If you look carefully, you'll see that we've used the end argument, but the string assigned to it is empty (it contains no characters at all).

What will happen now? Run the program in the editor to find out.

As the end argument has been set to nothing, the print() function outputs nothing too, once its positional arguments have been exhausted.

'''

print("My name is ", end="")
print("Monty Python.")