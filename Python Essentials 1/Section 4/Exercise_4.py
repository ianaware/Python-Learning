'''

Level of difficulty
Medium

Prerequisites
LAB 4.3.1.6

Objectives
Familiarize the student with:

projecting and writing parameterized functions;
utilizing the return statement;
utilizing the student's own functions.
Scenario
Your task is to write and test a function which takes two arguments (a year and a month) and returns the number of days for the given month/year pair (while only February is sensitive to the year value, your function should be universal).

The initial part of the function is ready. Now, convince the function to return None if its arguments don't make sense.


'''

def is_year_leap(year):

 if year % 400 == 0:
        return(True)
 elif year % 100 == 0:
        return(False)
 elif year % 4 == 0:
        return(True)
    

def days_in_month(year, month):
#
# Write your new code here.
#

    if month < 1 or month > 12:
        return None

    month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_year_leap(year):
        month_lengths[1] = 29
    
    return month_lengths[month - 1]

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
