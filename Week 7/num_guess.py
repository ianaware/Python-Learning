'''

Create a number guessing game:

The program should choose a random number between 1 and 100.
The user is then asked to guess the number.
Use a while loop to allow the user to keep guessing until they guess the number correctly.
After each guess, the program tells the user if their guess is too high or too low.
Once the user guesses the number, break out of the loop and print a congratulatory message.

'''

import random
num = random.randint(1, 100) #generate random number from 1 - 100
while True:  #Add this to start the loop 
            guess = input("Please guess the number between 1 and 100 or type 'quit' to end ") #get input (it will be string)
            if guess.lower() == "quit": #check if it matches then print message and end
                 print("Goodbye")
                 break
            try:
                guess_int = int(guess) #try this as it may break (case conversion)

                if guess_int > num:
                    print ("Too high") #check the guess against the random number generated
                elif guess_int < num:
                    print ("Too low")  #check the guess against the random number generated
                else:
                    print("Well done - you got it!")  #if it is matched display a message and end
                    break
            except ValueError:
                print("Invalid Input") #if the Try fails it will be an exception, invoke this exception type and print a message
                break