dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
phone_numbers = {'boss': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}
words = ["cat", "lion", "horse"]

print(dictionary)
print(phone_numbers)
print(empty_dictionary)

print(dictionary["cat"]) #print out the key "cat" from the dictionary
print(phone_numbers['Suzy']) #print out the key "Suzy" from the dictionary
print(dictionary["horse"]) #print out the key "horse" from the dictionary

for key in dictionary.keys():
    print(key, "->", dictionary[key]) #print out the key and value from the dictionary

#print(phone_numbers["john"]) #this will error out because "john" is not in the dictionary

for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "is not in the dictionary")
        
for key in sorted(dictionary.keys()):
    print(key, "->", dictionary[key]) #print out the key and value from the dictionary in sorted order
    
    