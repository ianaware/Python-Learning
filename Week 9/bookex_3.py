'''

To show looping through dictionaries

'''

counts = {'snow' : 1, 're' : 2, 'kitty' : 3} #create dictionary with keys and values
lst = list(counts.keys()) #creates a list of all the keys in the dictionary
print(lst) #print out list that is unsorted
lst.sort() #sort the keys in the list

for key in lst: #create loop with 'key' as loop variable to go through the list
    print(key, counts[key]) #print out the keys and values from the list that should now be sorted alphabetically
    
    