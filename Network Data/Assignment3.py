url = input("Enter the URL: ") #asks user to input the URL
import urllib.request #imports the urllib.request module
import xml.etree.ElementTree as ET #imports the xml.etree.ElementTree module

response = urllib.request.urlopen(url) #opens the URL
xml_data = response.read() #reads the xml data

root = ET.fromstring(xml_data) #parses the xml data

comment_counts = [] #creates an empty list
for comment in root.findall('.//comment'): #finds all the counts in the xml data
    comment_count = comment.find('count').text #finds the count in the xml data
    comment_counts.append(int(comment_count)) #appends the count to the list
    
total_comments = sum(comment_counts) #sums the total comments   
print(total_comments) #prints the total comments    





