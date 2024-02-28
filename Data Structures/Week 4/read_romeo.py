'''

Write a program to open the file romeo.txt and read it line by line.

For each line, split the line into a list of words using the split function.



'''

unique_words = [] #create an empty list

with open("C:\\Users\\ian.w\\OneDrive - AWARE CORPORATION LIMITED\\GitHub\\Python\\Python-Learning\\Data Structures\\Week 4\\romeo.txt") as File: #use \\ to escape backslashes in string literals
    for line in File: #read lines in the file
        print(line) #print them out
        words = line.split() #split each line in to a list of words called 'words' and store them
        for word in words: #go through all the words in the list
            if word not in unique_words: #go through and see which words are not in the list
                unique_words.append(word) #add them to the list

unique_words.sort() #arrange the words in the list in alphabetical order
print(unique_words)



