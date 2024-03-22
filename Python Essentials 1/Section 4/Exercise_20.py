tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
duplicates = tup.count(2)

print(duplicates)    # outputs: 

d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}

for item in (d1, d2):
    d3.update(item)
    
    # Write your code here.

print(d3)

my_list = ["car", "Ford", "flower", "Tulip"]

t =  tuple(my_list)

print(t)    # outputs:

colors = (("green", "#008000"), ("blue", "#0000FF"))

colors_dictionary = dict(colors)

print(colors_dictionary)

my_dictionary = {"A": 1, "B": 2}
copy_my_dictionary = my_dictionary.copy()
my_dictionary.clear()

print(copy_my_dictionary)