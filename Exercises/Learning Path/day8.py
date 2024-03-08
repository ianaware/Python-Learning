'''
Day 8: File Reading and Writing
• Write a program that reads a text file and prints its contents line by line.
• Modify the program to write a new file with the lines in uppercase.


'''

input_file_path = r'C:\Users\ian.w\OneDrive - AWARE CORPORATION LIMITED\GitHub\Python\Python-Learning\words.txt' #input file path
output_file_path = r'C:\Users\ian.w\OneDrive - AWARE CORPORATION LIMITED\GitHub\Python\Python-Learning\wordsupper.txt' #output file path

with open (input_file_path) as input_file, open (output_file_path, 'w') as output_file: #open input_file_path and store contents as input_file
    for line in input_file:  
        uppercase_line = line.upper() #create new variable and store uppercase content in it
        output_file.write(uppercase_line) #write uppercase content as output file
    
print("File has been converted to uppercase and saved.") #print output

#Read file

with open (input_file_path) as input_file: #open the input_file_path and store as input_file
    for line in input_file:  #go through all lines
       print(line) #print out each line
       
