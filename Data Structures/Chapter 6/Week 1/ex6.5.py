'''
Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. 
Convert the extracted value to a floating point number and print it out.

'''

text = "X-DSPAM-Confidence:    0.8475" # text to work with
#to_find_zero = text.find("0") #find 0 as string
#print (to_find_zero) #get character position of 0 (23)
#to_find_five = text.find("5")
#print (to_find_five) #get character position of 5 (28)
to_find_text = text[23:29] #extract the specific range of characters
to_find_float = float(to_find_text) #convert to float
print (to_find_float) #print value as float
#print(type(to_find_float)) #confirms that the data returned is float