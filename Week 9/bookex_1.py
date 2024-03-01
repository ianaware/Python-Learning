'''

Write a program that reads the words in words.txt and stores them as keys in a dictionary. It doesn't matter what the values are. 
Then you can use the in operator as a fast way to check whether a string is in the dictionary.

'''

word_dictionary = {}

fhand = open(r'C:\Users\ian.w\OneDrive - AWARE CORPORATION LIMITED\GitHub\Python\Python-Learning\words.txt') #open the file

for line in fhand:
    words = line.split()
    #print(words)
    for word in words:
        word = word.lower()
        if word in word_dictionary:
            word_dictionary[word] +=1 #increase the count
        else:
            word_dictionary[word] = 1
            
for word, count in word_dictionary.items(): #print each word and its count
    print(word, count) #output each word with its count
    