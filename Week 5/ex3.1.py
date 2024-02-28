hrs = input("Enter Hours:")
rate = input("Enter Rate:")
try:
    h = float(hrs)
    rate_num = float(rate)
except:
    print("Invalid input.  Please enter a number.")
    quit()
print(h, rate_num)
if h <= 40:
    pay = h * rate_num
else:
    # Calculate pay for first 40 hours
    base_pay = 40 * rate_num
    # Calculate overtime pay (time beyond 40 hours)
    overtime_pay = (h - 40) * (rate_num * 1.5) #This is because it has to get the number of hours above 40, after that it takes that number and multiplies by rate * 1.5 (OT pay)
    # Total pay is the sum of base pay and overtime pay
    pay = base_pay + overtime_pay

print(pay)