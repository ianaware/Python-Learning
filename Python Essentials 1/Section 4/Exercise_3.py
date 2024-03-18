'''

Estimated time
10-15 minutes

Level of difficulty
Easy

Objectives
Familiarize the student with:

projecting and writing parameterized functions;
utilizing the return statement;
testing the functions.
Scenario
Your task is to write and test a function which takes one argument (a year) and returns True if the year is a leap year, or False otherwise.

The seed of the function is already shown in the skeleton code in the editor.


'''

def is_year_leap(year):
#
# Write your code here.
#

    if year % 400 == 0:
        return(True)
    elif year % 100 == 0:
        return(False)
    elif year % 4 == 0:
        return(True)
    
 
    


test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"->",end="")
	result = is_year_leap(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
