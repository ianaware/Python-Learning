'''

Open the file mbox-short.txt and read it line by line. 
When you find a line that starts with 'From ' like the following line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). 

Then print out a count at the end.

Hint: make sure not to include the lines that start with 'From:'. 
Also look at the last line of the sample output to see how to print the count.



'''

fname = input("Enter file name: ")
if len(fname) < 1: #if len(fname) is less than 1, it means the string fname has no characters in it so no filename entered
    fname = r"C:\Users\ian.w\OneDrive - AWARE CORPORATION LIMITED\GitHub\Python\Python-Learning\Week 4\mbox-short.txt"

fh = open(fname)
count = 0  
    
for line in fh:
        if not line.startswith("From "):
            continue #go to next line
        words = line.split() #split in to lines
        email = words[1] #get the first element after a space (0 = From, 1 = stephen.marquard@uct.ac.za, 2 = Sat, 3 = Jan etc...)
        print(email) #print it out
        count = count + 1 #increment counter
            
print("There were", count, "lines in the file with From as the first word") #print out results