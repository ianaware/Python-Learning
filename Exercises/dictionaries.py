'''

Exercise: Word Count in a Sentence

Write a Python program that does the following:

Asks the user to input a sentence. 

For example, the user could enter "the cat sat on the mat".

The program should then split the sentence into words and create a dictionary where each key is a unique word from the sentence, and its value is the number of times that word appears in the sentence.

Finally, the program should print out each word and its corresponding count.


'''

word_count = {} #empty dictionary

user_input = input("Enter a sentence: ")
user_input.split() #split into lines
words = user_input.split() #chop the lines into words
for word in words: #go through all the words
    lower_word = word.lower() #make lowercase
    if lower_word in word_count: #checks if the word exists in the dictionary
        word_count[lower_word] += 1 #word has been seen multiple times
    else:
        word_count[lower_word] = 1 #word has been seen for the first time
        
for word, count in word_count.items():
    print(f"'{word}': {count} times") #count and print the results
