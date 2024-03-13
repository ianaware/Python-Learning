'''

Since the introduction of the Gregorian calendar (in 1582), the following rule is used to determine the kind of year:

if the year number isn't divisible by four, it's a common year;
otherwise, if the year number isn't divisible by 100, it's a leap year;
otherwise, if the year number isn't divisible by 400, it's a common year;
otherwise, it's a leap year.
Look at the code in the editor - it only reads a year number, and needs to be completed with the instructions implementing the test we've just described.

The code should output one of two possible messages, which are Leap year or Common year, depending on the value entered


'''

year = int(input("Enter a year: "))

if year % 4 != 0:
    print("Common Year") #if the year number isn't divisible by four, it's a common year;
elif year % 100 != 0:
    print("Leap Year") #otherwise, if the year number isn't divisible by 100, it's a leap year;
elif year % 400 != 0:
    print("Common Year")#otherwise, if the year number isn't divisible by 400, it's a common year;
else:
    print("Leap Year")#otherwise it's a leap year
