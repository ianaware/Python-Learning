'''

Exercise: Word Count in a Sentence

Objective: Write a Python program that reads a sentence from the user and counts how many times each word appears in that sentence. 

The program should then print each word and its corresponding count.

Steps:

Get User Input: Prompt the user to enter a sentence. 

For simplicity, you can assume the sentence does not contain any punctuation.

Split the Sentence into Words: Use the split() method to divide the sentence into individual words.

Initialize a Dictionary: Create an empty dictionary named word_count to store the count of each word.

Count the Words: Loop through the list of words from the sentence. For each word, update the word_count dictionary to keep track of how many times each word appears.

Print the Results: After counting all words, print out each word along with its count.

'''

word_count = {} #empty dictionary

user_input = input("Enter a sentence: ")
words = user_input.split() #split the sentence in to words
#print(words)
for word in words: #go through each word
    if word in word_count: #if word exists in dictionary (word_count)
        word_count[word] +=1 #increase the count
    else:
        word_count[word] = 1 #add the word with a count of 1 if it's not already in the dictionary

for word, count in word_count.items(): #print each word and its count
    print(word, count) #output each word with its count
    