'''

Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. 

Do not use the sum() function or a variable named sum in your solution.


'''

# Use the file name mbox-short.txt as the file name
count = 0 #initialise count to count lines
total = 0 #Add the floating point values


fname = input("Enter file name: ") #ask for file name
fh = open(fname) #create file handler
for line in fh: #go through each line
    line = line.rstrip() #remove whitespace
    if line.startswith("X-DSPAM-Confidence:"): #if line contains text
        colon_pos = line.find(':') #find the :
        number = float(line[colon_pos+1:]) #get value after the : as float
        count += 1 # Increment the count for each line starting with "X-DSPAM-Confidence:"
        total += number # Add the extracted floating-point value to the cumulative total

if count > 0: #checks to ensure there is at least one line counted to avoid division by zero, which is an important detail for calculating the average.
    average = total / count #work out the average
else:
    average = 0
print("Average spam confidence:", average) #print out the data
