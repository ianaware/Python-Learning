text = "X-DSPAM-Confidence:    0.8475" # text to work with

colon_pos = text.find(':')
print(colon_pos) #gives character 18

piece = text[colon_pos+2:] #Get data from character 18 to the end space
print(piece) #Output the data
value = float(piece) #convert the data to a float
print (value) #print out the value

