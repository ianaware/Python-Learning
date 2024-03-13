'''

 The most important tax, called the Personal Income Tax (PIT for short) had to be paid once a year, and was evaluated using the following rule:

if the citizen's income was not higher than 85,528 thalers, the tax was equal to 18% of the income minus 556 thalers and 2 cents (this was the so-called tax relief)
if the income was higher than this amount, the tax was equal to 14,839 thalers and 2 cents, plus 32% of the surplus over 85,528 thalers.
Your task is to write a tax calculator.

It should accept one floating-point value: the income.
Next, it should print the calculated tax, rounded to full thalers. There's a function named round() which will do the rounding for you - you'll find it in the skeleton code in the editor.


'''

income = float(input("Enter the annual income: "))

if income <= 85528:
    tax = 18 / 100 * income - 556.02 #18% of income - 556.02
    if tax < 0: #no tax is returned so if less than 0 then tax = 0
        tax = 0
else:
    surplus = income - 85528
    tax = 14839.02 + 32 / 100 * surplus 

tax = round(tax)
print("The tax is:", tax, "thalers")