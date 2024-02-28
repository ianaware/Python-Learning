h = input("Enter the number of hours: ") #Get string input
r = input("Enter the rate of pay: ") #Get string input

def computepay (h, r):
    hrs = float(h) #Convert string to float
    rate = float(r) #Convert string to float
    if hrs <= 40:
        pay = hrs * rate #Calculate pay
    elif hrs > 40:
        base_pay = 40 * rate
        overtime_pay = (hrs - 40) * (rate * 1.5)
        pay = base_pay + overtime_pay
    return pay

print('Pay', computepay(h, r))