fhand = open('mbox-short.txt') #open the file

for line in fhand: #start loop to go through each line
    line = line.rstrip() #remove whitespace
    print (line.upper()) #print file in uppercase
