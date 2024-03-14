'''

Scenario
The break statement is used to exit/terminate a loop.

Design a program that uses a while loop and continuously asks the user to enter a word unless the user enters "chupacabra" as the secret exit word, in which case the message "You've successfully left the loop." should be printed to the screen, and the loop should terminate.


'''
secret_word = "chupacabra"


while True:
    user_input = input("Enter a word: ")#enter a string
    if user_input != secret_word:
        continue
    else:
        print("You've successfully left the loop.")
        break
  



        