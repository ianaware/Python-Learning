'''

Estimated time
15-20 minutes

Level of difficulty
Easy

Objectives
improving the ability to use numbers, operators, and arithmetic operations in Python;
using the print() function's formatting capabilities;
learning to express everyday-life phenomena in terms of programming language.
Scenario
Your task is to prepare a simple code able to evaluate the end time of a period of time, given as a number of minutes (it could be arbitrarily large). The start time is given as a pair of hours (0..23) and minutes (0..59). The result has to be printed to the console.

For example, if an event starts at 12:17 and lasts 59 minutes, it will end at 13:16.

Don't worry about any imperfections in your code - it's okay if it accepts an invalid time - the most important thing is that the code produce valid results for valid input data.


'''

# Inputs from the user
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Calculate end time
end_minute = (mins + dura) % 60  # Find the new minutes
end_hour = (hour + (mins + dura) // 60) % 24  # Find the new hour, adjusting for any additional hours from minutes

# Print the end time
print(f"The event will end at {end_hour:02d}:{end_minute:02d}")