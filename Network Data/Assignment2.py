from urllib.request import urlopen
from bs4 import BeautifulSoup

url = input("Enter URL ")
count = int(input("Enter count: "))
position = int(input("Enter position: "))

for i in range(count):
    print("Retreiving: ", url)
    html = urlopen(url).read()
    soup = BeautifulSoup(html, 'lxml')
    
    tags = soup('a')
    url = tags[position -1].get('href', None)
    
    print("Last URL: ", url)
    
