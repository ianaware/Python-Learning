my_list = [456, 3,6,7,22,1,4]

largest = my_list[0]

for i in range(1, len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]     
        
print(largest) 

my_list2 = [673, 83, 633, 23,3]

largest2 = my_list2[0]

for i in my_list2:
    if i > largest2:
        largest2 = i
        
print(largest2)  

my_list3 = [1 , 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False

for i in range(len(my_list3)):
    found = my_list3[i] == to_find
    if found:
        break
if found:
    print("Element found at index ", i)
else:
    print("Absent")
    
drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]
hits = 0

for numbers in bets:
    if numbers in drawn:
        hits += 1
print(hits)