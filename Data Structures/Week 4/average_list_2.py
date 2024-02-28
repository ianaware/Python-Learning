#Create a list of numbers

num_list = [10, 5, 23, 56, 500]

#Calculate the sum of the numbers

num_list_sum = 0
num_list_count = 0

for numbers in num_list:
    num_list_sum = num_list_sum + numbers

#Calculate the count of the numbers in the list

num_list_count = len(num_list)

print("The average is: ", num_list_sum / num_list_count)

