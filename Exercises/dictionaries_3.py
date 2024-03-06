'''

Exercise
Now, let's put this into practice. Here's an exercise for you:

Create a dictionary called book that contains the following information about a book: 

title, author, and year of publication.
Print the author of the book.
Add a new key-value pair where the key is 'pages' and the value is the number of pages in the book.
Change the year of publication to a more recent year.
Use a for loop to print out each key and value in the dictionary.


'''
book = {'title': 'nineteen eighty four', 'author': 'george orwell', 'year_of_publication': '1949' }
print(book['author']) #print out the author
book['pages'] = '200' #add pages as a new key value pair
book['year_of_publication'] = 2024 #update year of publication

#now to use a for loop

for key in book: #loop through keys in dictionary
    print(key, book[key] ) #print out keys
    
    