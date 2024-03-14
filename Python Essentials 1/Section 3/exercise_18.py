'''
Create a for loop that counts from 0 to 10, and prints odd numbers to the screen. Use the skeleton below:

for i in range(1, 11):
    # Line of code.
        # Line of code.

'''

for i in range(1, 11):
    if i % 2 != 0: #if 0, meaning no remainder, then it's even, otherwise if it isn't 0 then there is a remainder
        print(i)
        
for i in range(1, 11):
    if i % 2 == 0: #if not 0, meaning a remainder, then it's odd, otherwise if it is 0 then there is no remainder
        print(i)
        
'''
Create a while loop that counts from 0 to 10, and prints odd numbers to the screen. Use the skeleton below:

'''

x = 0

while x <= 10:
   if x % 2 != 0:
       print(x)
   x += 1
   

'''
Create a program with a for loop and a break statement. 
The program should iterate over characters in an email address, exit the loop when it reaches the @ symbol, and print the part before @ on one line. 

Use the skeleton below:

'''

for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch, end = '')