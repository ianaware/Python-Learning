# Use words.txt as the file name
fname = input("Enter file name: ") #Ask for file name
fh = open(fname) #create handler for file name
for line in fh: #go through all lines in the file
    line = line.rstrip() #remove whitespace
    print(line.upper()) #convert all text to uppercase and output