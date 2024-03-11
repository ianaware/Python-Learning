'''

Estimated time
10 minutes

Level of difficulty
Easy

Objectives
becoming familiar with the concept of, and working with, variables;
performing basic computations and conversions;
experimenting with Python code.

cenario
Miles and kilometers are units of length or distance.

Bearing in mind that 1 mile is equal to approximately 1.61 kilometers, complete the program in the editor so that it converts:

miles to kilometers;
kilometers to miles.
Do not change anything in the existing code. Write your code in the places indicated by ###. Test your program with the data we've provided in the source code.




'''

kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.60934
kilometers_to_miles = kilometers * 0.621371

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

usd = 100
baht = 1000

usd_to_baht = usd * 35.46
baht_to_usd = baht * 0.02820

print(usd, "dollars is", round(usd_to_baht, 2), "baht")
print(baht, "baht is", round(baht_to_usd, 2), "dollars")