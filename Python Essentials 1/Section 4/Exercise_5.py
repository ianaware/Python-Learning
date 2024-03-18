'''
Estimated time
20-30 minutes

Level of difficulty
Medium

Prerequisites
LAB 4.3.1.6
LAB 4.3.1.7

Objectives
Familiarize the student with:

projecting and writing parameterized functions;
utilizing the return statement;
building a set of utility functions;
utilizing the student's own functions.
Scenario
Your task is to write and test a function which takes three arguments (a year, a month, and a day of the month) and returns the corresponding day of the year, or returns None if any of the arguments is invalid.


'''
def is_year_leap(year):
    if year % 400 == 0:
        return(True)
    elif year % 100 == 0:
        return(False)
    elif year % 4 == 0:
        return(True)
    

def days_in_month(year, month):
    if month < 1 or month > 12:
        return None

    month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_year_leap(year):
        month_lengths[1] = 29
    
    return month_lengths[month - 1]

def day_of_year(year, month, day):
    if year < 1 or month < 1 or month > 12 or day < 1 or day > days_in_month(year, month):
        return None

    day_count = day
    for m in range(1, month):
        day_count += days_in_month(year, m)
    return day_count    

print(day_of_year(2000, 12, 31))
