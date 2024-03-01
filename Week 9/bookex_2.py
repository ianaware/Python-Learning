try:
    with open(r"C:\Users\ian.w\OneDrive - AWARE CORPORATION LIMITED\GitHub\Python\Python-Learning\Week 9\romeo.txt") as fhand: #create file handler (fhand) for given file
        count = dict() #create en empty dictionary
        for line in fhand: #go through each line in the file
            words = line.split() #split each line in to words
            for word in words: #loop to go thorugh all the words
                word = word.lower() #convert them to lowercase for ease of use
                if word not in count: #checks if the word is not already a key in the dictionary 
                    count[word] = 1 # Initialize count for new word
                else:
                        count[word] += 1 #Increase count for existing word
except FileNotFoundError:
    print("File not found") #display message if file not found
    exit() #exit program
    
print(count) #print count of words in the dictionary

      