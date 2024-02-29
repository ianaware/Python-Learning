def count(word): #Create function
    count = 0 #set count to 0
    for letter in word: #go through each letter in word 'letter' = loop variable
        if letter == "a": #look for 'a'
            count = count + 1 #count them and keep score
    print(count) #print total

count("banana") #run function and pass string to work with ('word')