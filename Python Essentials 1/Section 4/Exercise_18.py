dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for english, french in dictionary.items():
    print(english, "->", french) #print out the key and value from the dictionary
    
for french, english in dictionary.items():
    print(french, "->", english) #print out the key and value from the dictionary   

for french in dictionary.values():
    print(french) #print out the values from the dictionary
    
dictionary["cat"] = "minou"
print(dictionary) #print out the dictionary after changing the value of the key "cat"

dictionary["swan"] = "cygne"
print(dictionary) #print out the dictionary after adding a new key and value

dictionary.update({"duck": "canard"})
print(dictionary) #print out the dictionary after adding a new key and value

del dictionary["dog"] #delete the key "dog" from the dictionary
print(dictionary) #print out the dictionary after deleting the key "dog"

dictionary.popitem() #delete the last key and value from the dictionary
print(dictionary) #print out the dictionary after deleting the last key and value