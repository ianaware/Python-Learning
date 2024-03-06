'''

Exercise: Squares and Filtering

In this exercise, you will create two lists using list comprehensions:

Square Numbers List: Create a list of the squares of numbers from 1 to 10. Use a list comprehension for this. Squaring a number is simply multiplying that number by itself (e.g., 2 squared is 2 * 2 = 4).

Even Squares List: From the list of squared numbers, create a new list containing only the squares that are even. Again, use a list comprehension to filter these out. A number is even if it is divisible by 2 without any remainder (in Python, number % 2 == 0 checks if a number is even).

'''

squares = [x**2 for x in range(1,11)] #create the list of squared numbers, so it's 1 x 2, 2 x2 , 3 x 2 etc for the numbers 1 to 10
print(squares) #print output

even_squares = [square for square in squares if square % 2 == 0] #find the even squares
print(even_squares)