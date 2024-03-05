'''
Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

'''
counts = {} #create empty dictionary

fhand = open('mbox-short.txt') #open the file

for line in fhand: #start loop to go through each line
    line = line.rstrip() #remove whitespace
    if line.startswith("From "): #if line contains text
       words = line.split() #split the line in to words
       sender = words[5] #look for the sixth value to get the hour
       time_parts = sender.split(':') #split y colon and store in new variable
       hour = time_parts[0] #get the hour value
       if hour in counts:
           counts[hour] += 1 #increment hours count if in dictionary
    else:
                counts[hour] = 1 #add to dictionary for the first time with a count of 1
for hour, count in sorted(counts.items()): print(hour, count)