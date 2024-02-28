#Use lists to search through text in a file

fhand = open('mbox-short.txt') #create file handler on file
for line in fhand: #Go through each line
    line = line.rstrip() #strip whitespace
    if not line.startswith('From '): continue #If 'From' isn't found continue the loop again
    words = line.split() #split the line if found
    print(words[2]) #output days of the week name
     