word_count  = 0
line_count = 0

with open (r'C:\Users\ian.w\OneDrive - AWARE CORPORATION LIMITED\GitHub\Python\Python-Learning\words.txt', 'r') as file:
    for line in file:
        print(line.strip())
        line_count += 1
        words = line.split()
        for word in words:
            word_count += 1
print("The number of lines is: ", line_count)
print("The number of words is: ", word_count)
        
 
        
    


        
    