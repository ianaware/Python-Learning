'''

 Open the file romeo.txt and read it line by line. 
 For each line, split the line into a list of words using the split() method. 
 The program should build a list of words. 
 For each word on each line check to see if the word is already in the list and if not append it to the list. 
 When the program completes, sort and print the resulting words in python sort() order as shown in the desired output.


'''

word_list = [] #create empty list

with open (r"C:\Users\ian.w\OneDrive - AWARE CORPORATION LIMITED\GitHub\Python\Python-Learning\Week 4\romeo.txt") as file: #open the file and print it, use 'r' as raw file
    for line in file:
        #print(line) #print out the lines of the document
        words = line.split() #make a new variable to split the lines in to words
        #print (words) #output the words
        for word in words: #go through all the words in the list
            if word not in word_list: 
                word_list.append(word) #add word to list

word_list.sort() #sort words alphabetically

print(word_list) #print the result
            
    
        
    