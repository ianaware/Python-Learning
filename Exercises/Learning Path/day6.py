'''

Day 6: Dictionaries
• Create a dictionary representing a book, including author, title, and year published.
• Write a program that prints all the keys and values of the dictionary.


'''

book = {"Author":"George Orwell", "Title": "Nineteen Eighty Four", "Year_Published": "1946"} #create dictionary

for key, value in book.items(): #add variables for key and value and use .items() on the dictionary
    print(f'{key}:{value}') #output the key and its value