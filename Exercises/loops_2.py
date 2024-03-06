'''

Exercise: Loop Control Statements

reak: Write a Python script that searches for a specified number in a list. 

Use a for loop to iterate through the list. 

If the number is found, print "Number found!" and then terminate the loop early with break. 

If the loop completes without finding the number, print "Number not found." You can define any list of numbers you like and choose any number to search for.

Example list: [3, 7, 42, 12, 9, 31], and you're searching for 12.

Continue: Create a Python script that uses a for loop to print all numbers from 1 to 10 except for 4 and 7. 

In this script, when you reach 4 or 7 in your loop, use the continue statement to skip printing these numbers.


'''

numbers = [3, 7, 42, 12, 9, 31] #create list
search = 12 #set number to search for
count = 1 #create count variable

for number in numbers: #create for loop, 'number' is the loop variable
    if search in numbers: #use in to check if the number to search for is in the list
        print(f'{search} was found') #print it was found
        break #exit the loop
    else:
        print(f'{search} not found') #print it was not found
        break #exit the loop
    
#Now for the use of Continue

while count <= 10:
     if count == 4 or count == 7: #check if the numbers are in the loop
        count +=1 #remember to increase count otherwise it gets stuck
        continue #skip and loop again
     else:
         print (count) #print count
         count += 1 #increment by 1
    
    
