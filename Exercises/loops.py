'''

Exercise
To help you get a hands-on understanding, here's a simple exercise: 

Create a Python script that uses a for loop to print out the numbers 1 through 10. 

Then, try to modify the script to use a while loop instead.

'''

#using for loop

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #create data

for number in numbers: #set loop variable in data
    print (number) #print result
    
#now in a while loop

counter = 1 #set counter

while counter <= 10: #check value of counter
    print(counter) #print counter
    counter +=1 #increase counter by 1

