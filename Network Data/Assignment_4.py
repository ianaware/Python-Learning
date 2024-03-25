url = input("Enter the URL: ") #asks user to input the URL
import urllib.request  # imports the urllib.request module
import json  # imports the json module

response = urllib.request.urlopen(url) #opens the URL
json_data = response.read() #reads the json data

data = json.loads(json_data) #loads the json data into a Python dictionary

comment_counts = [] #creates an empty list

comment_counts = [] # creates an empty list

for json_data in data['comments']: #finds all the counts in the json data
    comment_count = json_data['count'] #finds the count in the json data
    comment_counts.append(int(comment_count)) #appends the count to the list

total_comments = sum(comment_counts) #sums the total comments   
print(total_comments) #prints the total comments    





