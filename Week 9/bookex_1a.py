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
        word_dictionary[word] = None

test_word = "hardware" #set test word to check for

print("Here is the contents of your file:", word_dictionary) #print out dictionary

if test_word.lower() in word_dictionary: #convert test word to lowercase
    print("Test word", test_word, "is in the dictionary") #output if word is in the dictionary
else:
    print("Test word", test_word, "is not in the dictionary") #output if word is not in the dictionary
     