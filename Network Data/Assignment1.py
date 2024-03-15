from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'http://py4e-data.dr-chuck.net/comments_1985235.html'  # Replace 'URL' with your actual data URL
html = urlopen(url).read()

soup = BeautifulSoup(html, "html.parser")

total = 0
span_tags = soup('span')  # Retrieve all of the span tags
for tag in span_tags:
    # Extract the text content of the span tag, convert it to an integer, and add it to the total
    total += int(tag.contents[0])

print('Total sum:', total)
