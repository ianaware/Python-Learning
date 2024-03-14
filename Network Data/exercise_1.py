'''
This code imports urllib and we create a file handler, pass it a string, make a loop to go through the text line by line and then decode it and print the output.

'''

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())
    

counts = {}
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) +1
    print(counts)
