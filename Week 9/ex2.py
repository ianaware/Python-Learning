'''
Exercise: Daily Email Count
Objective: Write a program to read through the mbox-short.txt file and figure out the distribution by day of the week for the messages. The program should create a Python dictionary that maps each day of the week to the number of emails sent on that day.

Steps:

Initialize a Dictionary: Start by creating an empty dictionary named day_count.

Open and Read the File: Open the file mbox-short.txt for reading. 
Loop through each line of the file.
Identify the Desired Lines: Look for lines that start with "From" (like before, ensure it's the lines with email metadata, typically starting with "From " followed by a space, not lines starting with "From:" which are different).
Extract the Day of the Week: For each of these lines, split the line into words and identify the day of the week, which should be the third word in these lines (considering zero indexing, it would be at index 2).
Update the Dictionary: For each day of the week you extract, update your day_count dictionary. If the day isn't already a key in your dictionary, add it with a value of 1. If it is already a key, increment the value by 1.
Print the Results: After you've finished reading through the file and populating the dictionary, print out the day of the week and the number of emails sent on that day. This can be done by looping through the day_count dictionary.

'''

day_count = {} #empty dictionary

fhand = open(r"C:\Users\ian.w\OneDrive - AWARE CORPORATION LIMITED\GitHub\Python\Python-Learning\Week 4\mbox-short.txt") #open the file

for line in fhand:
    line = line.rstrip() #strip whitespace
    if line.startswith("From "): #look for thge lines with From
        words = line.split() #split each line in to words
        day = words[2] #from the words get the day name
        day_count[day] = day_count.get(day, 0) + 1


# Loop through each day and print the count of emails
for day, count in day_count.items():
    print(day, count)
    
    
    




