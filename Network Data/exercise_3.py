import requests
from bs4 import BeautifulSoup

url = "http://py4e-data.dr-chuck.net/comments_42.html" #URL to fetch

#Fetch the URL contents
response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')

print(soup.prettify)

for link in soup.find_all('a'):
    print(link) #print all links
    
for paragraph in soup.find_all('p'):
    print(paragraph) #print all paragraphs

for span in soup.find_all('span'):
    print(span) #print all span

total_sum = 0
for span in soup.find_all('span'):
    total_sum += int(span.text)

print("Total Sum: ", total_sum)
