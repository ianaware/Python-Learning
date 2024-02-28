file = input("Enter a file name: ") #ask to input file name

if file == "easter egg": #check file name to see if it matches
        print("Congratulations! This is an easter Egg") #print something
        quit() #quit

try:
    fhand = open(file) #open the file
 
except:
    print("File cannot be opened - ", file) #if file cannot be opened, print something
    exit()


for line in fhand: #start loop to go through each line offile that can be opened
    line = line.rstrip() #remove whitespace from file
    print (line.upper()) #print file in uppercase
