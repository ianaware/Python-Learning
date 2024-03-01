'''

Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.


'''

sender_count = {} #empty dictionary
max_count = 0
max_sender = None

fhand = open('mbox-short.txt') #open the file

for line in fhand: #start loop to go through each line
    line = line.rstrip() #remove whitespace
    if line.startswith("From "): #if line contains text
       words = line.split() #split the line in to words
       sender = words[1] #look for the second word value (sender email address)
       sender_count[sender] = sender_count.get(sender, 0) + 1 #checks if sender is already a key in the sender_counts dictionary:
   
for sender, count in sender_count.items():
    if count > max_count: #if the count is greater than the current max count
        max_count = count #update max count with the highest value
        max_sender = sender #update max sender to this sender

print(max_sender, max_count)

           
       
            
            
            
        
    