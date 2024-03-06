import re
with open(r"C:\Users\ian.w\OneDrive - AWARE CORPORATION LIMITED\GitHub\Python\Python-Learning\Week 10\regex_sum_1985233.txt", 'r') as file:
    text = file.read() #open file and read it
    numbers = re.findall(r'[0-9]+', text) #go throuth the text 'text' and look for all the integers

total_sum = sum(int(number) for number in numbers) #create a variable called total_sum, convert to integer and then use a for loop to go through it

print(f"The total sum of numbers in the file is {total_sum} ") #print the output